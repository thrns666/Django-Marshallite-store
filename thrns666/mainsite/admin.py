from django.contrib import admin
from .models import *

# Register your models here.

class MainsiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'availability', 'cat')
    list_display_links = ('title',)
    search_fields = ('title', 'description')
    list_editable = ('availability', 'price')
    list_filter = ('cat', 'price', 'availability')

class LastCategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name',)

admin.site.register(Product, MainsiteAdmin)
admin.site.register(LastCategories, LastCategoriesAdmin)


