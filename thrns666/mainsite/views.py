from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *
from tokens import *

menu = ['Главная страница', 'Каталог', 'Доставка', 'Обратная связь', 'Сотрудничество']


# Create your views here.
def index(request):
    db_returns = ShopTable.objects.all()
    return render(request, 'mainsite/index.html', {'title': 'Главная страница', 'head_menu': menu, 'categories': db_returns, 'font_awesome_token': font_awesome_token})

def about(request):
    return render(request, 'mainsite/about.html', {'title': 'О данном сайте', 'main_menu': menu})

def bot_page(request):
    db_returns = DataTable.objects.all()
    return render(request, 'mainsite/bot_page.html', {'title': 'Страница запросов', 'db_obj': db_returns})
