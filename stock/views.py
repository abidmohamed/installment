from dal import autocomplete
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.
from category.models import Category
from customer.models import Customer
from product.models import ProductType, Product, ProductColor
from sellorder.models import Order, OrderItem
from stock.forms import  StockForm, StockProductForm
from stock.models import  Stock, StockProduct


def add_stock(request):
    if request.method == 'GET':
        stockform = StockForm()
    elif request.method == 'POST':
        stockform = StockForm(request.POST)
        if stockform.is_valid():
            stockform.save()
            return redirect('stock:stock_list')
    context = {'stockform': stockform}
    return render(request, 'stock/add_stock.html', context)


def stock_list(request):
    stocks = Stock.objects.all()
    context = {
        'stocks': stocks,
    }
    return render(request, 'stock/list_stock.html', context)


def all_stock_list(request):
    stocks = Stock.objects.all()
    context = {
        'stocks': stocks,
    }
    return render(request, 'stock/list_stock.html', context)


def update_stock(request, pk):
    stock = Stock.objects.get(id=pk)
    stockform = StockForm(instance=stock)
    if request.method == 'POST':
        stockform = StockForm(request.POST, instance=stock)
        if stockform.is_valid():
            stockform.save()
            return redirect('stock:stock_list')
    context = {'stockform': stockform}
    return render(request, 'stock/add_stock.html', context)


def delete_stock(request, pk):
    stock = Stock.objects.get(id=pk)
    context = {'stock': stock}
    if request.method == 'POST':
        stock.delete()
        return redirect('stock:stock_list')
    return render(request, 'stock/delete.html', context)


def add_stockproduct(request):
    # check if product exist in stock already
    if request.method == 'GET':
        stockproductform = StockProductForm()
    elif request.method == 'POST':
        stockproductform = StockProductForm(request.POST)
        if stockproductform.is_valid():
            stockproduct = stockproductform.save(commit=False)
            items = StockProduct.objects.all().filter(stock=request.POST['stock'])

            itemexist = 1
            if len(items) > 0:
                for item in items:
                    if item.product.id == stockproduct.product.id:
                        item.quantity += stockproduct.quantity
                        item.save()
                        itemexist = 2
                        print("ALL FINE HERE 1")
                if itemexist == 1:
                    stockproduct.save()
                    itemexist = 0
                    print("ALL FINE HERE 2")
            else:
                itemexist = 0
                if itemexist == 0:
                    stockproduct.save()
                    print("ALL FINE HERE 3")

            return redirect('stock:stock_list')
    context = {'stockproductform': stockproductform}
    return render(request, 'stockproduct/add_stockproduct.html', context)


def stockproduct_list(request, pk):
    stock = Stock.objects.get(id=pk)
    stockproducts = StockProduct.objects.all().filter(stock=stock)

    context = {
        'stockproducts': stockproducts,
    }
    return render(request, 'stockproduct/list_stockproduct.html', context)


def all_stockproduct_list(request):
    stockproducts = StockProduct.objects.all().filter(quantity__gt=0)
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'stockproducts': stockproducts,
    }
    return render(request, 'stockproduct/all_list_stockproduct.html', context)


def order_stockproduct_list(request):
    stockproducts = StockProduct.objects.all()
    customers = Customer.objects.all()
    if request.method == 'POST':
        # get submitted orders
        chosenproducts = request.POST.getlist("products")
        chosencustomer = request.POST.getlist("customers")
        if len(chosenproducts) != 0 and len(chosencustomer) != 0:
            customer = Customer.objects.get(id=chosencustomer[0])
            sellorder = Order()
            sellorder.customer = customer
            sellorder.save()
            for product in chosenproducts:
                currentproduct = StockProduct.objects.get(id=product)
                # print(currentproduct)
                OrderItem.objects.create(
                    order=sellorder,
                    stockproduct=currentproduct,
                    price=currentproduct.product.sellpricenormal,
                    weight=currentproduct.product.weight,
                    quantity=1,
                )
            return redirect(f'../../sellorder/confirm_order/{sellorder.pk}')

    context = {
        'customers': customers,
        'stockproducts': stockproducts,
    }
    return render(request, 'stockproduct/order_list_stockproduct.html', context)


def stockproduct_detail(request, id):
    stockproduct = get_object_or_404(StockProduct, id=id)

    context = {
        'stockproduct': stockproduct,

    }
    return render(request, 'stockproduct/detail.html', context)


def stockproductcategory_list(request, pk):
    categories = Category.objects.all()
    category = Category.objects.get(id=pk)
    stockproducts = StockProduct.objects.all().filter(category=category)
    customer = Customer.objects.get(user=request.user)
    customertype = customer.customer_type
    context = {
        'category': category,
        'categories': categories,
        'stockproducts': stockproducts,
        'customertype': customertype,
        'customer': customer,
    }
    return render(request, 'stockproduct/list_stockproduct.html', context)


def stockproduct_quantityalert(request):
    products = Product.objects.all()
    for product in products:
        stockproductsalert = StockProduct.objects.all().filter(quantity__lte=product.alert_quantity)
    context = {
        'stockproductsalert': stockproductsalert,
    }

    return render(request, 'stockproduct/stock_alert_list.html', context)


def update_stockproduct(request, pk):
    stockproduct = StockProduct.objects.get(id=pk)
    stockproductform = StockProductForm(instance=stockproduct)
    if request.method == 'POST':
        stockproductform = StockProductForm(request.POST, instance=stockproduct)
        if stockproductform.is_valid():
            stockproductform.save()
            return redirect('stock:stock_list')
    context = {'stockproductform': stockproductform}
    return render(request, 'stockproduct/add_stockproduct.html', context)


def delete_stockproduct(request, pk):
    stockproduct = StockProduct.objects.get(id=pk)
    context = {'stockproduct': stockproduct}
    if request.method == 'POST':
        stockproduct.delete()
        return redirect('stock:stock_list')
    return render(request, 'stockproduct/delete.html', context)


# class CompleteProduct(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         if not self.request.user.is_authenticated:
#             return Product.objects.none()
#
#         qs = Product.objects.all()
#
#         if self.q:
#             qs = qs.filter(Q(name__icontains=self.q) | Q(ref__icontains=self.q))
#
#         return qs


# def productautocomplete(request):
#     if 'term' in request.GET:
#         # print(request.GET.get('term'))
#         qs = Product.objects.filter(
#             Q(name__icontains=request.GET.get('term')) | Q(ref__icontains=request.GET.get('term')))
#         products = list()
#         # print(qs)
#         for product in qs:
#             # print(product.product.name)
#             # pk = product.product.pk
#             # print("appending...")
#             products.append(
#                 str(product.pk) + " " + product.name
#             )
#
#         #  print(products)
#         return JsonResponse(products, safe=False)
#     context = {}
#     return render(request, 'stockproduct/add_stockproduct.html', context)

# product properties
def loadtypes(request):
    requestproduct = request.GET.get('product')
    print(request.GET)
    # ['id','name']
    splitedproduct = requestproduct.split()

    product_id = splitedproduct[0]
    # get Product
    product = Product.objects.get(id=product_id)
    # get types and colors
    types = ProductType.objects.all().filter(product=product)
    colors = ProductColor.objects.all().filter(product=product)
    # print(colors)
    context = {
        'types': types,
        'product_id': product_id
    }
    return render(request, 'stockproduct/get_type.html', context)


def loadcolors(request):
    requestproduct = request.GET.get('product')
    # ['id','name']
    splitedproduct = requestproduct.split()

    product_id = splitedproduct[0]
    # get Product
    product = Product.objects.get(id=product_id)
    # get types and colors
    colors = ProductColor.objects.all().filter(product=product)
    # print(colors)
    context = {
        'colors': colors,
        'product_id': product_id
    }
    return render(request, 'stockproduct/get_color.html', context)


def loadprice(request):
    requestproduct = request.GET.get('product')
    # ['id','name']
    splitedproduct = requestproduct.split()

    product_id = splitedproduct[0]
    # get Product
    product = Product.objects.get(id=product_id)
    # get types and colors
    price = product.buyprice
    print(price)
    return HttpResponse(price)
