from django_filters import FilterSet, DateFilter, CharFilter
from .models import *


class ProductFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='contains', label='Название')
    price = CharFilter(field_name='price', lookup_expr='contains', label='Цена')
    
    class Meta:
        model = Product
        fields = ['name', 'price', 'category']

