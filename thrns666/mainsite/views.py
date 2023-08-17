from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *
from .forms import *
from .utils import DataMixin


# Create your views here.
class HomePage(ListView):
    model = Slider
    template_name = 'mainsite/index.html'
    context_object_name = 'slides'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Интернет-магазин Marshalite'
        return context



class CatalogProducts(ListView):
    model = Product
    template_name = 'mainsite/new_cat.html'
    context_object_name = 'db_products'
    # allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.kwargs['category_slug'] != 'index':
            context['title'] = LastCategories.objects.get(slug=self.kwargs['category_slug']).name
            context['selected_cat'] = LastCategories.objects.get(slug=self.kwargs['category_slug'])
            print(LastCategories.objects.get(slug=self.kwargs['category_slug']).sub_cat)
        else:
            context['title'] = 'Категории товаров'

        return context

    def get_queryset(self):
        if self.kwargs['category_slug'] != 'index':
            return Product.objects.filter(cat_id__slug=self.kwargs['category_slug'])
        else:
            return ''


class ProductPage(DataMixin, DetailView):
    model = Product
    template_name = 'mainsite/product_page.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['product']
        return context


def about(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = AddProductForm()

    return render(request, 'mainsite/about.html', {'form': form, 'title': 'О данном сайте'})

class BotPage(DataMixin, ListView):
    model = Product

    template_name = 'mainsite/bot_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='footerok')
        print(context)
        return dict(list(context.items()) + list(c_def.items()))



