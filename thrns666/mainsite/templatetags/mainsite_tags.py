from django import template
from mainsite.models import *

register = template.Library()

@register.simple_tag(name='main_cats')
def get_main_cats():
    return MainCategories.objects.all()

@register.simple_tag(name='sub_cats')
def get_sub_cats():
    return SubCategories.objects.all()

@register.simple_tag(name='last_cats')
def get_last_cats():
    return LastCategories.objects.all()