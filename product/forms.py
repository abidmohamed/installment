from django.forms import ModelForm, modelformset_factory
from django import forms
from product.models import Product, ProductType, ProductColor


class ProductForm(ModelForm):
    class Meta:
        model = Product

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name...'}),
            'ref': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'REF...'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Desc...'}),
            'category': forms.Select(attrs={'class': 'form-control '}),
            'stock': forms.Select(attrs={'class': 'form-control '}),
            'image': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Image...'}),
            'sellpricenormal': forms.NumberInput(attrs={'class': 'form-control '}),
            # 'sellpricesemi_grou': forms.NumberInput(attrs={'class': 'form-control '}),
            # 'sellpricegrou': forms.NumberInput(attrs={'class': 'form-control '}),
            'buyprice': forms.NumberInput(attrs={'class': 'form-control '}),
            # 'alert_quantity': forms.NumberInput(attrs={'class': 'form-control '}),
            # 'box_quantity': forms.NumberInput(attrs={'class': 'form-control '}),
            'weight': forms.NumberInput(attrs={'class': 'form-control '}),

        }

        fields = ['category', 'name', 'ref', 'desc', 'image', 'stock', 'sellpricenormal',
                  'buyprice', 'weight']


ProductTypeFormset = modelformset_factory(
    ProductType,
    fields=('name', ),
    extra=1,
)


ProductColorFormset = modelformset_factory(
    ProductColor,
    fields=('name',),
    extra=1,
)
