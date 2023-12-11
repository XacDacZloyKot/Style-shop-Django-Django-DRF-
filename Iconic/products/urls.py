from django.urls import path, re_path


from django.conf.urls.static import static

from Iconic import settings
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('item/<slug:item_slug>/', show_item, name='item'),
    path('catalog/<slug:cat_slug>/', show_catalog, name='category'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('for_man/', for_man, name='for_man'),
    path('for_women/', for_women, name='for_women'),
    path('login/', login, name='login'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)