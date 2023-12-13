from django.urls import path, re_path


from django.conf.urls.static import static

from Iconic import settings
from .views import *

urlpatterns = [
    path('', CatalogHome.as_view(), name='home'),
    path('item/<slug:item_slug>/', ShowItem.as_view(), name='item'),
    path('catalog/<slug:cat_slug>/', ShowCatalog.as_view(), name='category'),
    path('about/', about, name='about'),
    path('addpage/', AddItem.as_view(), name='add_page'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)