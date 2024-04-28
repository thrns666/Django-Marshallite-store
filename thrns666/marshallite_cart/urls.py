from django.urls import path
from .views import *


urlpatterns = [
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('item_clear/<int:product_id>/', item_clear, name='item_clear'),
    path('item_increment/<int:product_id>/', item_increment, name='item_increment'),
    path('item_decrement/<int:product_id>/', item_decrement, name='item_decrement'),
    path('cart-detail/', cart_detail, name='cart_detail')
]
