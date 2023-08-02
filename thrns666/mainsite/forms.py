from django import forms
from .models import *
from django.core.exceptions import ValidationError


class AddProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'
    class Meta:
        model = Product
        fields = ['title', 'photo', 'description', 'price', 'availability', 'cat', 'slug']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-input'}),
            'description' : forms.Textarea(attrs={'cols' : 60, 'rows' : 10})
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
                    if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',']:
                        continue
                    else:
                        raise ValidationError('Неверно введено число стоимости')
            else:
                raise ValidationError('Цена указана неверно')
        else:
            raise ValidationError('Возможно вы не поставили пробел между стоимостью и "руб."')




