from .models import *

menu = [{'title': "Каталог", 'url_name': 'home'},
        {'title': "Добавить", 'url_name': 'add_page'},
        {'title': "О нас", 'url_name': 'about'}]


class DataMixin:
    paginate_by = 12
    def get_user_context(self, **kwargs):
        context = kwargs
        
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
            
        context['menu'] = user_menu
        
        if 'cat_shearch' not in context:
            context['cat_shearch'] = 0
        
        if 'category_selected' not in context:
            context['category_selected'] = 0
        return context