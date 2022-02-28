from django.db import models


# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length=250, null=True)
    lastname = models.CharField(max_length=250, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    national_number = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_joined = models.DateField(null=True)

    debt = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.firstname + " " + self.lastname
#
# class ClientPayment(models.Model):
#     customer = models.ForeignKey(Client, null=True, on_delete=models.DO_NOTHING)
#     amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     payment_date = models.DateField()
#     date_created = models.DateTimeField(auto_now_add=True, null=True)


class Contract(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

