from django.db import models
from django.urls import reverse


class DataTable(models.Model):
    title = models.CharField(max_length=115, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    contacts = models.CharField(max_length=150, blank=True)
    photo = models.ImageField(upload_to='photos/%y/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Slider(models.Model):
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='photos/%y/')
    text_on_photo_head = models.CharField(blank=True, max_length=255)
    text_on_photo_lower = models.CharField(blank=True, max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    link = models.CharField(blank=True, max_length=255)


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

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'
        ordering = ['title', 'availability', 'price', 'cat']

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})


# Stash this
class UserCart(models.Model):

    product_id = models.ForeignKey('Product', on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['quantity']
