from django.db import models
from product.models import Product, ProductType, ProductColor
from category.models import Category


# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=250, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'stock'
        verbose_name_plural = 'stocks'

    def __str__(self):
        return self.name


class StockProduct(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, null=True, on_delete=models.CASCADE)
    type = models.ForeignKey(ProductType, null=True, on_delete=models.CASCADE)
    color = models.ForeignKey(ProductColor, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('product',)
        verbose_name = 'stockproduct'
        verbose_name_plural = 'stockproducts'

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        self.category = self.product.category
        # if self.image:
        #    self.image = get_thumbnail(self.image, '570x320').url
        super(StockProduct, self).save(*args, **kwargs)

    def get_types(self):
        types = self.product.types.all()
        return types

    def get_colors(self):
        colors = self.product.colors.all()
        return colors
