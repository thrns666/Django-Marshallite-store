from django.db import models
from django.urls import reverse


# Create your models here.

class DataTable(models.Model):
    title = models.CharField(max_length=115, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    contacts = models.CharField(max_length=150, blank=True)
    photo = models.ImageField(upload_to='photos/%y/')
    description = models.TextField(blank=True)


    def __str__(self):
        return self.title


class MainCategories(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Категория 1го уровня'
        verbose_name_plural = 'Категории 1го уровня'
        ordering = ['id', 'name']
    def __str__(self):
        return self.name

class SubCategories(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    main_cat = models.ForeignKey('MainCategories', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Категория 2го уровня'
        verbose_name_plural = 'Категории 2го уровня'
        ordering = ['id', 'name']

    def __str__(self):
        return self.name


class LastCategories(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    sub_cat = models.ForeignKey('SubCategories', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория 3го уровня'
        verbose_name_plural = 'Категории 3го уровня'
        ordering = ['id', 'name']


    def get_absolute_url(self):
        return reverse('catalog', kwargs={'category_slug': self.slug})

class Product(models.Model):
    title = models.CharField(max_length=115, blank=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%y/')
    price = models.CharField(max_length=20, default='0 руб.', verbose_name='Стоимость')
    availability = models.BooleanField(default=True, verbose_name='Наличие')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    cat = models.ForeignKey('LastCategories', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'
        ordering = ['title', 'availability', 'price', 'cat']



    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})