from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from tokens import *


# Create your views here.
def index(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'mainsite/index.html', context=context)


def about(request):
    return render(request, 'mainsite/about.html', {'title': 'О данном сайте'})


def catalog(request, category_slug):
    if category_slug == 'index':
        db_products = None
        context = {
            'title': 'Каталог',
            'db_products': db_products
        }

        return render(request, 'mainsite/new_cat.html', context=context)

    elif LastCategories.objects.get(slug=category_slug):
        db_products = Product.objects.filter(cat_id=LastCategories.objects.get(slug=category_slug).pk)
        title = LastCategories.objects.get(slug=category_slug).name
        context = {
            'title': title,
            'db_products': db_products
        }

        return render(request, 'mainsite/new_cat.html', context=context)

    else:
        return Http404


def product_page(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    context = {
        'title': product.title,
        'product': product,
    }

    return render(request, 'mainsite/product_page.html', context=context)
