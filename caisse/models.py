from django.db import models


# Create your models here.
class Caisse(models.Model):
    caisse_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    updated = models.DateTimeField(auto_now=True, null=True)


class CaisseHistory(models.Model):
    caisse_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Bank(models.Model):
    bank_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    updated = models.DateTimeField(auto_now=True)


class BankHistory(models.Model):
    bank_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
