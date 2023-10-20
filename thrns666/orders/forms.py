from django import forms
from .models import Order
from django.core.exceptions import ValidationError


class OrderCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    first_name = forms.CharField(label='Имя',
                                 widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    # phone = forms.CharField(label='Ваш номер телефона', widget=forms.TextInput(attrs={
    #     'placeholder': '+375 (хх) ххх хх хх'
    # }))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'placeholder': 'Адрес вашей эл. почты'}))

    class Meta:
        model = Order
        fields = ('first_name', 'email')

    # def clean_phone(self):
    #     phone = self.cleaned_data['phone']
    #     if len(phone) != 13 or len(phone) != 17:
    #         if not phone.startswith('+375'):
    #             raise ValidationError('Некорректный номер телефона, номер должен начинаться с "+375"')
    #         else:
    #             for i in phone[1:].split():
    #                 if not i.isdigit:
    #                     raise ValidationError('Номер телефона должен состоять из цифр')
    #     else:
    #         raise ValidationError('Неверная длина номера телефона')
    #
    #     return phone
