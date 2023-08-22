from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('about/', about, name='about'),
    path('bot/', BotPage.as_view(), name='testfooter'),
    path('catalog/<slug:category_slug>/', CatalogProducts.as_view(), name='catalog'),
    path('product/<slug:product_slug>/', ProductPage.as_view(), name='product'),
    # path('login/, ')
    path('register/', RegisterUser.as_view(), name='register')
]