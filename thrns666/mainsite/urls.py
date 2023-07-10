from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('about/', about, name='about'),
    path('catalog/<slug:category_slug>/', catalog, name='catalog'),
    path('product/<slug:product_slug>/', product_page, name='product')
]