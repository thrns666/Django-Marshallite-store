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
