from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя',
                                 widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    phone = forms.CharField(label='Ваш номер телефона',
                                 widget=forms.TextInput(attrs={'placeholder': '+375 (хх) ххх хх хх'}))
    class Meta:
        model = Order
        fields = ('first_name', 'phone')

