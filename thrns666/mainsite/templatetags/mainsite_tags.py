from django import template
from mainsite.models import *
from tokens import *

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

@register.simple_tag(name='bootstrap_link_token')
def get_bootstrap_token():
    return bootstrap_link_integrity

@register.simple_tag(name='bootstrap_script_token')
def get_bootstrap_token():
    return bootstrap_script_integrity

@register.simple_tag(name='fonts_token')
def get_fonts_token():
    return font_awesome_token