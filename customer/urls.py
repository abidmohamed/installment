from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('add_customer', views.add_customer, name='add_customer'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('update_customer/<str:pk>', views.update_customer, name='update_customer'),
    path('customer_detail/<str:pk>', views.customer_detail, name='customer_detail'),
    path('delete_customer/<str:pk>', views.delete_customer, name='delete_customer'),

    path('customer_ordering', views.customer_ordering, name='customer_ordering'),

    path('add_contract/<str:pk>', views.add_contract, name='add_contract'),
    path('saving_contract/<str:pk>', views.saving_contract, name='saving_contract'),
    path('contract_list', views.contract_list, name='contract_list'),

]
