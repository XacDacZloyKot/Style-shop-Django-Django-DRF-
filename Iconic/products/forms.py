from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.core.exceptions import ValidationError
from .models import *


class AddProductForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"
        
    class Meta:
        model = Product
        fields = ['name', 'description', 'short_description','image', 'price', 'slug', 'category', 'quantity', 'is_available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form__input'}),
            'short_description': forms.TextInput(attrs={'class': 'form__input'}),
            'slug': forms.TextInput(attrs={'class': 'form__input'}),
            'description': forms.Textarea(attrs={'cols':60, 'rows': 10}),
        }
        
    def clean_name(self): #  Пользовательская валидация
        name = self.cleaned_data['name']
        if len(name)>200:
            raise forms.ValidationError("Длинна превышает 200 символов")
        return name
    