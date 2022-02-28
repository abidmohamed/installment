from django.urls import path
from . import views

app_name = 'sellorder'

urlpatterns = [

    path('sellorder_list', views.sellorder_list, name='sellorder_list'),
    path('confirm_order/<str:pk>', views.confirm_order, name='confirm_order'),

]
