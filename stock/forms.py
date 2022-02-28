from django.forms import ModelForm
from django import forms

from product.models import ProductType, ProductColor, Product
from stock.models import Stock, StockProduct


class StockForm(ModelForm):
    class Meta:
        model = Stock

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name...'}),

        }

        fields = ['name']


class StockProductForm(ModelForm):
    class Meta:
        model = StockProduct

        widgets = {
            'stock': forms.Select(attrs={'class': 'form-control '}),
            'product': forms.TextInput(attrs={'id': 'product'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        fields = ['product', 'stock', 'quantity', 'type', 'color']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].queryset = ProductType.objects.none()
        self.fields['color'].queryset = ProductColor.objects.none()

        # if the user hit submit but didn't choose a color & type we fill it directly from product field
        if 'product' in self.data:
            try:
                requestproduct = int(self.data.get('product'))
                splitedproduct = requestproduct.split()
                product = Product.objects.get(id=splitedproduct[0])
                self.fields['type'].queryset = ProductType.objects.filter(product=product).order_by('name')
                self.fields['color'].queryset = ProductColor.objects.filter(product=product).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
