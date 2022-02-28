from django.shortcuts import render
import datetime

# Create your views here.
from buyorder.models import BuyOrder
from customer.models import Customer, Contract
from sellorder.models import Order
from supplier.models import Supplier


def home(request):
    # now time
    now = datetime.datetime.now()
    allcustomers = Customer.objects.all()
    allsuppliers = Supplier.objects.all()

    thismonthsellorders = Order.objects.all().filter(created__year=now.year, created__month=now.month)
    thismonthbuyorders = BuyOrder.objects.all().filter(created__year=now.year, created__month=now.month)

    customerscount = Customer.objects.all().count()
    supplierscount = Supplier.objects.all().count()

    orderscount = Order.objects.all().filter(created__year=now.year).count()
    buyorderscount = BuyOrder.objects.all().filter(created__year=now.year).count()
    ordersfacturedcount = Order.objects.all().filter(factured=True).count()

    endingcontracts = Contract.objects.all().filter(end_date__year=now.year, end_date__month=now.month)

    # sell orders total
    totalsellorders = 0
    totalbuyorders = 0
    for order in thismonthsellorders:
        totalsellorders += order.get_total_cost()
    # Buy orders total
    for order in thismonthbuyorders:
        totalbuyorders += order.get_total_cost()
    # Total customers Debt
    totaldebt = 0
    for customer in allcustomers:
        totaldebt += customer.debt

    # Total suppliers Credit
    totalcredit = 0
    for supplier in allsuppliers:
        totalcredit += supplier.credit

    # Most Products bought
    allOrders = {}
    for order in thismonthsellorders:
        orderitems = order.items.all()
        for item in orderitems:
            if item.stockproduct.product.name in allOrders:
                allOrders[item.stockproduct.product.name] += item.stockproduct.quantity
            else:
                allOrders[item.stockproduct.product.name] = item.stockproduct.quantity

    context = {
        'customerscount': customerscount, 'orderscount': orderscount, 'buyorderscount': buyorderscount,
        'supplierscount': supplierscount, 'ordersfacturedcount': ordersfacturedcount,
        'totalsellorders': totalsellorders, 'totalbuyorders': totalbuyorders, 'totaldebt': totaldebt,
        'totalcredit': totalcredit, 'allOrders': allOrders, 'endingcontracts': endingcontracts
    }

    return render(request, 'dashboard.html', context)
