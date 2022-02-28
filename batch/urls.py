from django.urls import path
from . import views

app_name = 'batch'

urlpatterns = [

    path('create_batch/<str:pk>', views.create_batch, name='create_batch'),
    path('batch_list', views.batch_list, name='batch_list'),
    path('batch_pay/<str:pk>', views.batch_pay, name='batch_pay'),

]