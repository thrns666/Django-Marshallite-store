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


class ShopTable(models.Model):
    title = models.CharField(max_length=115, blank=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%y/')
    price = models.CharField(max_length=20, default='0')
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('product', kwargs={'product_id': self.pk})
