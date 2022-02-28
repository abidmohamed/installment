from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from customer.forms import CustomerForm,  ContractForm
from customer.models import Customer, Contract


def add_customer(request):
    customer_form = CustomerForm()
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer = customer_form.save()
            return redirect('customer:customer_list')

    context = {
        'customer_form': customer_form
    }
    return render(request, 'customer/add_customer.html', context)


def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'customer/list_customer.html', context)


def update_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer_form = CustomerForm(instance=customer)
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, instance=customer)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('customer:customer_list')
    context = {
        'customer_form': customer_form
    }
    return render(request, 'customer/add_customer.html', context)


def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    context = {
        'customer': customer
    }
    if request.method == 'POST':
        customer.delete()
        return redirect('customer:customer_list')
    return render(request, 'customer/delete_customer.html', context)


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    context = {
        'customer': customer
    }
    return render(request, 'customer/detail.html', context)


# customer chosen for ordering
def customer_ordering(request):
    customers = Customer.objects.all()
    if request.method == 'POST':
        # get submitted customer
        chosencustomer = request.POST.getlist("customers")
        if len(chosencustomer) != 0:
            # create customer object
            currentcustomer = Customer.obejects.get(id=chosencustomer)
            print(currentcustomer)

    context = {
        'customers': customers
    }
    return render(request, 'customer/list_customer_for_order.html', context)


# Contract
def add_contract(request, pk):
    customer = Customer.objects.get(id=pk)
    contrat = Contract()
    contrat.customer = customer
    contrat.save()
    return redirect(f'../saving_contract/{contrat.pk}')


def saving_contract(request, pk):
    contract = Contract.objects.get(id=pk)
    contractForm = ContractForm(instance=contract)
    if request.method == 'POST':
        contractForm = ContractForm(request.POST, instance=contract)
        if contractForm.is_valid():
            contractForm.save()
            return redirect('customer:customer_list')

    context = {
        'contractForm': contractForm,
    }
    return render(request, 'contract/add_contract.html', context)


def contract_list(request):
    contracts = Contract.objects.all()
    context = {
        'contracts': contracts,
    }
    return render(request, 'contract/list_contract.html', context)
