from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from customer.models import Customer, Contract


class CustomerForm(ModelForm):
    class Meta:
        model = Customer

        fields = ('firstname', 'lastname', 'phone', 'address', 'national_number', 'email', 'debt')


# Contract
class ContractForm(ModelForm):
    class Meta:
        model = Contract

        fields = ('start_date', 'end_date', )