from .models import *

menu = [{'title': "Каталог", 'url_name': 'home'},
        # {'title': "Для неё", 'url_name': 'for_women'},
        # {'title': "Для него", 'url_name': 'for_man'},
        {'title': "Добавить", 'url_name': 'add_page'},
        {'title': "О нас", 'url_name': 'about'}]


class DataMixin:
    paginate_by = 12
    def get_user_context(self, **kwargs):
        context = kwargs
        
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(3)
            
        context['menu'] = user_menu
        
        
        if 'category_selected' not in context:
            context['category_selected'] = 0
        return context