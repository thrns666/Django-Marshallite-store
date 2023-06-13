from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('about/', about, name='about'),
    path('bot_page/', bot_page, name='bot_page'),
    path('catalog/', catalog, name='catalog'),
    path('products/', product_catalog, name='products_catalog'),
    path('product/', product_page, name='product')
]