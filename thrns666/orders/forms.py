from django import forms
from .models import Order
from django.core.exceptions import ValidationError


# class OrderCreateForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     class Meta:
#         model = Order
