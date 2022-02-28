from django.urls import path
from . import views

app_name = 'billingbuyorder'

urlpatterns = [

    path('bill_list', views.bill_list, name='bill_list'),
    path('bill_pdf/<str:pk>', views.bill_pdf, name='bill_pdf'),

]
