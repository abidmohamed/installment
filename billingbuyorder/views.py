from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from xhtml2pdf import pisa

from billingbuyorder.models import BuyOrderBilling


def bill_list(request):
    bills = BuyOrderBilling.objects.all()
    context = {'bills': bills}

    return render(request, 'billingbuyorder/list_bill.html', context)


def delete_bill(request, pk):
    bill = get_object_or_404(BuyOrderBilling, id=pk)
    context = {'bill': bill}
    if request.method == 'POST':
        bill.delete()

        return redirect('billingbuyorder:bill_list')
    return render(request, 'billingbuyorder/list_bill.html', context)


def bill_pdf(request, pk):
    bill = get_object_or_404(BuyOrderBilling, id=pk)
    html = render_to_string('billingbuyorder/pdf.html', {'bill': bill})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=bill_{bill.id}.pdf'
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
