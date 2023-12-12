from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .utils import *

class CatalogHome(DataMixin, ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'
    
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Каталог")
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self) -> QuerySet[Any]: #  Какие записи должны быть на странице отображены
        return Product.objects.filter(is_available=True)
        

def about(request):
    return render(request, 'products/about.html', {'title': 'О сайте'})


class AddItem(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddProductForm
    template_name = 'products/addpage.html'
    login_url = reverse_lazy('home')
    raise_exception = True #  Генерирует 403(нет доступа) если не авторизован
    # success_url = reverse_lazy('home') #  Перенаправление после добавления поста
    
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление товара")
        return dict(list(context.items()) + list(c_def.items()))
        # context['title'] = "Добавление товара"
        # return context

def for_man(request):
    return HttpResponse("Для него")


def for_women(request):
    return HttpResponse("Для неё")


def login(request):
    return HttpResponse("Регистрация")


class ShowItem(DataMixin,DetailView):
    model = Product
    template_name = 'products/item.html'
    slug_url_kwarg = 'item_slug'
    context_object_name = 'products'

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['products'].name)
        return dict(list(context.items()) + list(c_def.items()))
    

class ShowCatalog(DataMixin,ListView):
    models = Product
    template_name = 'products/index.html'
    context_object_name = 'products'
    allow_empty = False #  404 при отсутсвии записей
    
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Категория: " + str(context['products'][0].category), category_selected=context['products'][0].category_id)
        return dict(list(context.items()) + list(c_def.items()))
        # context['title'] = "Категория: " + str(context['products'][0].category)
        # context['category_selected'] = context['products'][0].category_id
        # return context

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['cat_slug'], is_available=True)
    

def archive(request, year):
    if int(year)>2023:
        # raise Http404()
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам {year}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
