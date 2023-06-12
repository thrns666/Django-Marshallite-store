from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('about/', about, name='about'),
    path('bot_page/', bot_page, name='bot_page'),
    path('catalog/', catalog, name='catalog')
]