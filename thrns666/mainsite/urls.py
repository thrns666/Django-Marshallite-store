from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('about/', about, name='about'),
    path('catalog/<slug:category_slug>/', CatalogProducts.as_view(), name='catalog'),
    path('product/<slug:product_slug>/', ProductPage.as_view(), name='product')
]