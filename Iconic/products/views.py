from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from .filters import *
from .models import *
from .forms import *
from .utils import *

class CatalogHome(DataMixin, ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'
    
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Каталог", form=FilterProductForm(self.request.GET), cat_shearch=1)
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self) -> QuerySet[Any]: #  Какие записи должны быть на странице отображены
        # filters = {}
        # name = self.request.GET.get('name')
        # price = self.request.GET.get('price')
        # category = self.request.GET.get('category')
        # if name:
        #     filters['name__contains'] = name
        # if price:
        #     filters['price__contains'] = price
        # if category:
        #     filters['category'] = category
        # new_context = Product.objects.filter(**filters)
        # return new_context

        # return Product.objects.filter(is_available=True) МОЕ
        
        queryset = super().get_queryset()
        st_filter = ProductFilter(self.request.GET, queryset)
        return st_filter.qs

        

class about(DataMixin, TemplateView):
    template_name = 'products/about.html'
    
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="О нас")
        return dict(list(context.items()) + list(c_def.items()))
    
    # return render(request, 'products/about.html', {'title': 'О сайте'})


def logout_user(request):
    logout(request)
    return redirect('login')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'products/login.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    
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
    
    
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'products/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')    
    


def archive(request, year):
    if int(year)>2023:
        # raise Http404()
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам {year}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
