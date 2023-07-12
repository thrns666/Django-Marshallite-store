from django import forms
from .models import *

class AddProductForm(forms.Forms):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    availability = forms.BooleanField()
    price = forms.CharField(max_length=150)
    cat = forms.ModelChoiceField(queryset=LastCategories.objects.all())

