from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import LoginView, PasswordResetView, LogoutView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.db.models import Q
from orders.models import Order
from .forms import *
from .utils import DataMixin
from .models import Product


# Create your views here.
class HomePage(DataMixin, ListView):
    model = Slider
    template_name = 'mainsite/index.html'
    context_object_name = 'slides'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Интернет-магазин Marshalite')
        context = {**context, **c_def}
        return context
        # context | c_def if python ver >= 3.9


class CatalogProducts(DataMixin, ListView):
    paginate_by = 10
    model = Product
    template_name = 'mainsite/new_cat.html'
    context_object_name = 'db_products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        m_cats = MainCategories.objects.all()
        s_cats = SubCategories.objects.all()
        l_cats = LastCategories.objects.all()

        if self.kwargs['category_slug'] != 'index':
            l_cats_category_slug_obj = LastCategories.objects.get(slug=self.kwargs['category_slug'])
            c_def = self.get_user_context(title=l_cats_category_slug_obj.name, selected_cat=l_cats_category_slug_obj, m_cats=m_cats, s_cats=s_cats, l_cats=l_cats)
            print(c_def['title'])
        else:
            c_def = self.get_user_context(title='Категории товаров', m_cats=m_cats, s_cats=s_cats, l_cats=l_cats)

        context = {**context, **c_def}
        return context

    def get_queryset(self):
        if self.kwargs['category_slug'] != 'index':
            return Product.objects.filter(cat_id__slug=self.kwargs['category_slug'])
        else:
            return ''


class InformationPage(DataMixin, TemplateView):
    template_name = 'mainsite/info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(info='Информация размещенная на данной странице может быть чем угодно')
        context = {**context, **c_def}
        return context


class SearchPage(DataMixin, ListView):
    model = Product
    template_name = 'mainsite/search_page.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        obj_list = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        print(obj_list)
        return obj_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Поиск')
        context = {**context, **c_def}
        return context


class ProductPage(DataMixin, DetailView):
    model = Product
    template_name = 'mainsite/product_page.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['product'])
        context = {**context, **c_def}
        return context


class UserProfile(DataMixin, DetailView):
    template_name = 'mainsite/account_page.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return get_object_or_404(User, id=self.request.user.id)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(user_orders=Order.objects.filter(user_id=self.request.user.id))
        print(context)
        context = {**context, **c_def}
        return context


class PasswordResetUser(DataMixin, PasswordResetView):
    form_class = PasswordResetForm
    template_name = 'mainsite/password_reset.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        print(context)
        context = {**context, **c_def}
        return context


class LogInUser(DataMixin, LoginView):
    authentication_form = LoginUserForm
    template_name = 'mainsite/login.html'

    def get_user_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return {**context, **c_def}


class LogoutUser(DataMixin, LogoutView):
    def get_user_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context, **c_def}


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'mainsite/register.html'
    success_url = reverse_lazy('login')

    def get_user_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context, **c_def}
