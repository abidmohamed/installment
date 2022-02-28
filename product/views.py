from django.shortcuts import render, redirect

# Create your views here.
from category.models import Category
from product.forms import ProductForm, ProductTypeFormset, ProductColorFormset
from product.models import Product, ProductType, ProductColor


def add_product(request):
    if request.method == 'GET':
        productform = ProductForm()
    elif request.method == 'POST':
        productform = ProductForm(request.POST, request.FILES)
        if productform.is_valid():
            product = productform.save()
            return redirect(f'../product/add_product_type/{product.pk}')
    context = {'productform': productform}
    return render(request, 'product/add_product.html', context)


def product_list(request, pk):
    category = Category.objects.get(id=pk)
    products = Product.objects.all().filter(category=category)
    context = {
        'products': products,
    }
    return render(request, 'product/list_product.html', context)


def all_product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'product/all_product_list.html', context)


def update_product(request, pk):
    product = Product.objects.get(id=pk)
    productform = ProductForm(instance=product)
    if request.method == 'POST':
        productform = ProductForm(request.POST, request.FILES, instance=product)
        if productform.is_valid():
            productform.save()
            return redirect('/')
    context = {'productform': productform}
    return render(request, 'product/add_product.html', context)


def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    if request.method == 'POST':
        product.delete()
        return redirect('/')
    return render(request, 'product/delete.html', context)


def add_type(request, pk):
    product = Product.objects.get(id=pk)
    productypeformset = ProductTypeFormset(queryset=ProductType.objects.none())
    if request.method == 'POST':
        productypeformset = ProductTypeFormset(request.POST)
        if productypeformset.is_valid():
            for typeform in productypeformset:
                producttype = typeform.save(commit=False)
                producttype.product = product
                producttype.save()

            return redirect(f'../add_product_color/{product.pk}')
    context = {
        'productypeformset': productypeformset,
    }
    return render(request, 'product/add_type.html', context)


def add_color(request, pk):
    product = Product.objects.get(id=pk)
    productcolorformset = ProductColorFormset(queryset=ProductColor.objects.none())
    if request.method == 'POST':
        productcolorformset = ProductColorFormset(request.POST)
        if productcolorformset.is_valid():
            for colorform in productcolorformset:
                productcolor = colorform.save(commit=False)
                productcolor.product = product
                productcolor.save()

            return redirect('/')
    context = {
        'productcolorformset': productcolorformset,
    }
    return render(request, 'product/add_color.html', context)


