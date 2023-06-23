from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *
from tokens import *


# Create your views here.
def index(request):
    context = {
        'title': 'Главная страница',
        'font_awesome_token': font_awesome_token
    }
    return render(request, 'mainsite/index.html', context=context)


def about(request):
    return render(request, 'mainsite/about.html', {'title': 'О данном сайте', 'main_menu': menu, 'font_awesome_token': font_awesome_token})


def bot_page(request):
    db_returns = DataTable.objects.all()
    return render(request, 'mainsite/bot_page.html', {'title': 'Страница запросов', 'db_obj': db_returns, 'font_awesome_token': font_awesome_token})


def catalog(request):
    db_main_catalog = MainCategory.objects.all()
    db_sub_catalog = SubCategories.objects
    db_last_catalog = LastCategories.objects
    context = {
        'title': 'Каталог',
        'db_main_cat': db_main_catalog,
        'db_sub_cat': db_sub_catalog,
        'db_last_cat': db_last_catalog,
        'font_awesome_token': font_awesome_token
    }
    return render(request, 'mainsite/catalog_page.html', context=context)


def product_catalog(request, category_id):
    db_returns = Product.objects.filter(cat_id=category_id)
    context = {
        'title': LastCategories.objects.get(id=category_id).name,
        'db_obj': db_returns,
        'font_awesome_token': font_awesome_token
    }
    return render(request, 'mainsite/products_catalog.html', context=context)




def product_page(request, product_id):
    db_returns = Product.objects.get(pk=product_id)
    context = {
        'title': db_returns.title,
        'db_obj': db_returns,
        'font_awesome_token': font_awesome_token,
        'product_id': product_id
    }
    return render(request, 'mainsite/product_page.html', context=context)