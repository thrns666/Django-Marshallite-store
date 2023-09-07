
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', cache_page(50)(HomePage.as_view()), name='homepage'),
    path('about/', about, name='about'),
    path('catalog/<slug:category_slug>/', cache_page(60)(CatalogProducts.as_view()), name='catalog'),
    path('product/<slug:product_slug>/', cache_page(15)(ProductPage.as_view()), name='product'),
    path('login/', LogInUser.as_view(), name='login'),
    path('change-password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('user-logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/', cart_detail, name='cart_detail')
]