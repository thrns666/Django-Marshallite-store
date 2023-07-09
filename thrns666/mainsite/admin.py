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
    search_fields = ('name',)

class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_cat', 'slug')
    search_fields = ('name',)


class MainCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'slug')
    search_fields = ('name',)


admin.site.register(Product, MainsiteAdmin)
admin.site.register(LastCategories, LastCategoriesAdmin)
admin.site.register(SubCategories, SubCategoriesAdmin)
admin.site.register(MainCategories, MainCategoriesAdmin)


