
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('about/', about, name='about'),
    path('catalog/<slug:category_slug>/', CatalogProducts.as_view(), name='catalog'),
    path('product/<slug:product_slug>/', ProductPage.as_view(), name='product'),
    path('login/', LogInUser.as_view(), name='login'),
    path('change-password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('user-logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register')
]