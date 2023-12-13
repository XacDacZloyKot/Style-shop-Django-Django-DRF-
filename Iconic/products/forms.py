from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserModel, AuthenticationForm
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
    

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form__input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form__input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form__input'}))
    password2 = forms.CharField(label='Пароль повтор', widget=forms.PasswordInput(attrs={'class': 'form__input'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widget = {
            'username': forms.TextInput(attrs={'class': 'form__input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form__input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form__input'}),
        }
        

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form__input'}))
    password = forms.CharField(label='Логин', widget=forms.PasswordInput(attrs={'class': 'form__input'}))
    
    
class FilterProductForm(forms.Form):
    name = forms.CharField(label='Название', max_length=50, required=False)
    price = forms.DecimalField(label='Стоимость', required=False)
    category = forms.ModelChoiceField(label='Категория', 
    queryset= ProductCategory.objects.all(), empty_label='', required=False)
