from django.urls import path
from .views import order_create, user_orders_list

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('orders-list/', user_orders_list, name='orders_list')
]
