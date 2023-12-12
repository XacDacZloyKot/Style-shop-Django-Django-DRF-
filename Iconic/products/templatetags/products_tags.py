from django import template
from products.models import *
from django.db.models import Count


register = template.Library()

menu = [{'title': "Каталог", 'url_name': 'home'},
        {'title': "Для неё", 'url_name': 'for_women'},
        {'title': "Для него", 'url_name': 'for_man'},
        {'title': "Добавить", 'url_name': 'add_page'},
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
    
        # user_menu = menu.copy()
        # if not self.request.user.is_authenticated:
        #     user_menu.pop(1)
            
        # context['menu'] = user_menu
        
        # user_menu = menu.copy()
        # if not self.request.user.is_authenticated:
        #     user_menu.pop(1)
            
        # context['menu'] = user_menu
    
    return {"menu": menu}

@register.inclusion_tag('products/tags/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        # cats = ProductCategory.objects.all()
        cats = ProductCategory.objects.annotate(Count('product'))
    else:
        cats = ProductCategory.objects.annotate(Count('product')).order_by(sort)
    return {"cats": cats, "cat_selected": cat_selected}