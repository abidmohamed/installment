from django.shortcuts import render, redirect

# Create your views here.
from batch.forms import OriginalBatchFrom
from batch.models import OngoinglBatch
from customer.models import Customer
from payments.forms import CustomerPaymentForm
from sellorder.models import Order


def create_batch(request, pk):
    sellorder = Order.objects.get(id=pk)
    batchform = OriginalBatchFrom(request.POST)
    if request.method == 'POST':
        batchform = OriginalBatchFrom(request.POST)
        if batchform.is_valid():
            batch = batchform.save(commit=False)
            batch.customer = sellorder.customer
            ongoingbatch = OngoinglBatch()
            ongoingbatch.customer = batch.customer
            ongoingbatch.amount = batch.amount
            ongoingbatch.period = batch.period
            ongoingbatch.save()
            return redirect('batch:batch_list')

    context = {
        'batchform': batchform,
        'sellorder': sellorder,
    }

    return render(request, 'batch/create.html', context)


def batch_list(request):
    batches = OngoinglBatch.objects.all().filter(period__gt=0)
    context = {
        'batches': batches
    }
    return render(request, 'batch/list.html', context)


def batch_pay(request, pk):
    batch = OngoinglBatch.objects.get(id=pk)
    customerpayment = CustomerPaymentForm()
    if request.method == 'POST':
        customerpayment = CustomerPaymentForm(request.POST)
        if customerpayment.is_valid():
            cp = customerpayment.save(commit=False)
            print(cp.pay_status)
            # if cash then save directly else show cheque to be filled
            cp.customer = batch.customer
            cp.customer.debt -= batch.amount
            print(cp.customer.debt)
            cp.customer.save()
            # TODO: Uncomment this one
            # cp.user = request.user.id
            cp.amount = batch.amount
            cp.save()
            # one batch payed
            batch.period -= 1
            batch.save()
            if cp.pay_status == "Cheque":
                return redirect(f"../../payments/create_customer_cheque/{cp.pk}")
            return redirect("batch:batch_list")

    context = {
        'customerpayment': customerpayment
    }
    return render(request, 'batch/pay.html', context)
