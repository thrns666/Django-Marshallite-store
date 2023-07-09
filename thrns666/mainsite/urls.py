from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('about/', about, name='about'),
    #path('bot_page/', bot_page, name='bot_page'),
    path('catalog/<int:category_id>/', catalog, name='catalog'),
    # path('products/<int:category_id>/', product_catalog, name='products_catalog'),
    path('product/<int:product_id>/', product_page, name='product')
]