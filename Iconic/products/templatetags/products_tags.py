from django import template
from products.models import *

register = template.Library()

menu = [{'title': "Каталог", 'url_name': 'home'},
        {'title': "Для неё", 'url_name': 'for_women'},
        {'title': "Для него", 'url_name': 'for_man'},
        {'title': "Добавить", 'url_name': 'addpage'},
        {'title': "О нас", 'url_name': 'about'},
        {'title': "Войти", 'url_name': 'login'}]

@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return ProductCategory.objects.all()
    else:
        return ProductCategory.objects.filter(pk=filter)

@register.simple_tag(name='get_navmenu')
def show_navmenu():
    return {"menu": menu}

@register.inclusion_tag('products/tags/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = ProductCategory.objects.all()
    else:
        cats = ProductCategory.objects.order_by(sort)
    return {"cats": cats, "cat_selected": cat_selected}