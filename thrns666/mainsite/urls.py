from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('cart/', include('marshallite_cart.urls')),
    path('info/', InformationPage.as_view(), name='info'),
    path('', cache_page(5)(HomePage.as_view()), name='homepage'),
    path('catalog/<slug:category_slug>/', cache_page(5)(CatalogProducts.as_view()), name='catalog'),
    path('search/', SearchPage.as_view(), name='search_result'),
    path('product/<slug:product_slug>/', cache_page(15)(ProductPage.as_view()), name='product'),
    path('login/', LogInUser.as_view(), name='login'),
    path('user/profile/', UserProfile.as_view(), name='profile_cabinet'),
    path('change-password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('user-logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register')
]