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
from django.urls import include, path
from django.conf.urls.static import static
from Iconic import settings
from products.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/v1/productlist/', ProductAPIView.as_view(), name='api'),
    path('api/v1/productlist/<int:pk>/', ProductAPIView.as_view(), name='api_put'),
    path('', include('products.urls')),
    
]

handler404 = pageNotFound