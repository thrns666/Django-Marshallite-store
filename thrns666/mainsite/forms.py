from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *
from django.core.exceptions import ValidationError


class LoginUserForm(AuthenticationForm):
    username = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Почта'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))

    class Meta:
        fields = ('username', 'password')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Ваш номер телефона', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+375 (хх) ххх хх хх'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Почта'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повтор пароля'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) != 13 or len(phone) != 17:
            if not phone.startswith('+375'):
                raise ValidationError('Некорректный номер телефона, номер должен начинаться с "+375"')
            else:
                for i in phone[1:].split():
                    if not i.isdigit:
                        raise ValidationError('Номер телефона должен состоять из цифр')
        else:
            raise ValidationError('Неверная длина номера телефона')

        return phone


class AddProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'
    class Meta:
        model = Product
        fields = ['title', 'photo', 'description', 'price', 'availability', 'cat', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 215:
            raise ValidationError('Длина превышает 215 символов')

        return title

    def clean_price(self):
        price = self.cleaned_data['price']
        if len(price.split()) == 2:
            if 'руб.' in price:
                for i in price.split()[0]:
                    if i.isdigit or i == ',':
                        continue
                    else:
                        raise ValidationError('Неверно введено число стоимости')
            else:
                raise ValidationError('Цена указана неверно')
        else:
            raise ValidationError('Возможно вы не поставили пробел между стоимостью и "руб."')
