"""
URL configuration for Iconic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from Iconic import settings
from products.views import *
from rest_framework import routers

# region <Custom Router>
class MyCustomRouter(routers.SimpleRouter):
    routes = [
        routers.Route(url=r'^{prefix}/$',
                      mapping={'get': 'list'},
                      name='{basename}-list',
                      detail=False,
                      initkwargs={'suffix': 'List'}),
        routers.Route(url=r'^{prefix}/{lookup}$',
                mapping={'get': 'retrieve'},
                name='{basename}-detail',
                detail=True,
                initkwargs={'suffix': 'Detail'})
    ]    
# endregion

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    
    
    path('api/v1/product-control/', ProductAPIList.as_view()),
    path('api/v1/product-control/<int:pk>/', ProductAPIUpdate.as_view()),
    path('api/v1/product-control-del/<int:pk>/', ProductAPIDestroy.as_view()),
    
    path('api/v1/', include(router.urls)), # https://127.0.0.1:8000/api/v1/product/ Viewset
    
    path('api/v1/category/', ProductCategoryAPIList.as_view(), name='category_api_get_post'), # get Class
    path('api/v1/categorydetail/<int:pk>/', ProductCategoryAPIDetailView.as_view(), name='category_detail_api'), # for item
    path('', include('products.urls')),
    
]

handler404 = pageNotFound