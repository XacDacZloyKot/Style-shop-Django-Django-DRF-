from django import forms
from .models import *


class AddProductForm(forms.Form):
    name = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    description = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows': 10}))
    short_description = forms.CharField(max_length=64)
    price = forms.DecimalField(decimal_places=2, max_digits=8)
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all())
    