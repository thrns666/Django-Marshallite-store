from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import *
from .utils import DataMixin


# Create your views here.
class HomePage(DataMixin, ListView):

    model = Slider
    template_name = 'mainsite/index.html'
    context_object_name = 'slides'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Интернет-магазин Marshalite')
        context = {**context, **c_def}
        return context # context | c_def if python ver >= 3.9



class CatalogProducts(DataMixin, ListView):
    paginate_by = 7
    model = Product
    template_name = 'mainsite/new_cat.html'
    context_object_name = 'db_products'
    # allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.kwargs['category_slug'] != 'index':
            c_def = self.get_user_context(title=LastCategories.objects.get(slug=self.kwargs['category_slug']).name, selected_cat=LastCategories.objects.get(slug=self.kwargs['category_slug']))
            print(LastCategories.objects.get(slug=self.kwargs['category_slug']).sub_cat)
        else:
            c_def = self.get_user_context(title='Категории товаров')

        context = {**context, **c_def}
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
        c_def = self.get_user_context(title=context['product'])
        print(context)
        context = {**context, **c_def}
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
        context = {**context, **c_def}
        return context


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'mainsite/register.html'
    success_url = reverse_lazy('login')

    def get_user_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context, **c_def}



