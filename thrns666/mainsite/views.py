from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

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
    return render(request, 'mainsite/about.html', {'title': 'О данном сайте', 'font_awesome_token': font_awesome_token})


def catalog(request, category_id=0):
    db_products = Product.objects.filter(cat_id=category_id)

    if category_id:
        selected_category = category_id
        title = LastCategories.objects.get(pk=category_id).name
    else:
        selected_category = 0
        title = 'Каталог'

    context = {
        'title': title,
        'db_products': db_products,
        'selected_category': selected_category,
        'font_awesome_token': font_awesome_token
    }
    return render(request, 'mainsite/new_cat.html', context=context)


def product_page(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'title': product.title,
        'product': product,
        'font_awesome_token': font_awesome_token,
        'product_id': product_id
    }
    return render(request, 'mainsite/product_page.html', context=context)
