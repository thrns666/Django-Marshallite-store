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
    return render(request, 'mainsite/about.html', {'title': 'О данном сайте', 'main_menu': menu, 'font_awesome_token': font_awesome_token})


def bot_page(request):
    db_returns = DataTable.objects.all()
    return render(request, 'mainsite/bot_page.html', {'title': 'Страница запросов', 'db_obj': db_returns, 'font_awesome_token': font_awesome_token})


def catalog(request):
    db_returns = ShopTable.objects.all()
    return render(request, 'mainsite/catalog_page.html', {'title': 'Каталог', 'db_obj': db_returns, 'font_awesome_token': font_awesome_token})


def product_catalog(request):
    db_returns = ShopTable.objects
    context = {
        'title': 'Каталог чего-то',
        'db_obj': db_returns,
        'font_awesome_token': font_awesome_token
    }
    return render(request, 'mainsite/products_catalog.html', context=context)


def product_page(request, product_id):
    db_returns = ShopTable.objects.get(pk=product_id)
    print(type(db_returns))
    context = {
        'title': 'Страница товара',
        'db_obj': db_returns,
        'font_awesome_token': font_awesome_token,
        'product_id': product_id
    }
    return render(request, 'mainsite/product_page.html', context=context)