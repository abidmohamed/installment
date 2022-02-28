from django.shortcuts import render, redirect

# Create your views here.
from batch.forms import OriginalBatchFrom
from customer.models import Customer
from sellorder.models import Order
from stock.models import StockProduct


# confirmation get order object from the stock view
def confirm_order(request, pk):
    sellorder = Order.objects.get(id=pk)
    # get customer to add debt
    customer = Customer.objects.get(id=sellorder.customer.pk)
    if request.method == 'POST':
        prices = request.POST.getlist('prices')
        quantities = request.POST.getlist('quantities')
        for index, item in enumerate(sellorder.items.all()):
            # get the price and value of each element
            # Saving the orderitem
            item.price = prices[index]
            item.quantity = quantities[index]
            item.save()
            # Reducing the sold products from stock
            stockitems = StockProduct.objects.all().filter(stock=item.stockproduct.product.stock)
            itemexist = 1
            #     # check if stock doesn't have the product
            if len(stockitems) > 0:
                # stock has products check if product exist
                for stockitem in stockitems:
                    # the same product exist
                    if stockitem.product.id == item.stockproduct.product.id:
                        stockitem.quantity -= int(item.quantity)
                        stockitem.save()
                        itemexist = 2
                        #                 # operation done same product plus the new quantity

                if itemexist == 1:
                    #             # stock not empty product doesn't exist in it
                    #             # create new stockproduct
                    StockProduct.objects.create(
                        product=item.stockproduct.product,
                        quantity=int(item.quantity),
                        # type=item.type,
                        # color=item.color,
                        category=item.stockproduct.product.category,
                        stock=item.stockproduct.product.stock
                    )
            else:
                #         # stock is empty
                itemexist = 0
                if itemexist == 0:
                    # create new stockproduct
                    StockProduct.objects.create(
                        product=item.stockproduct.product,
                        quantity=int(item.quantity),
                        # type=item.type,
                        # color=item.color,
                        category=item.stockproduct.product.category,
                        stock=item.stockproduct.product.stock
                    )
        sellorder.save()
        # customer debt
        customer.debt += sellorder.get_total_cost()
        customer.save()
        # batch (installement) page
        return redirect(f'../../batch/create_batch/{sellorder.pk}')
    context = {
        'customer': customer,
        'sellorder': sellorder,
    }
    return render(request, 'sellorder/sellorder_confirmation.html', context)


def sellorder_list(request):
    sellorders = Order.objects.all()
    context = {
        'sellorders': sellorders
    }
    return render(request, 'sellorder/list_sellorder.html', context)
