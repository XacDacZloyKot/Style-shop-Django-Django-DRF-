from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *

class CatalogHome(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'
    
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Каталог"
        context['category_selected'] = 0
        return context
    
    def get_queryset(self) -> QuerySet[Any]: #  Какие записи должны быть на странице отображены
        return Product.objects.filter(is_available=True)

# Create your views here.
# def index(request):
#     products = Product.objects.all()
#     context = {
#         'products':products, 
#         'title': 'Каталог', 
#         'category_selected': 0,
#         }
    
#     return render(request, 'products/index.html', context=context)

        

def about(request):
    return render(request, 'products/about.html', {'title': 'О сайте'})

class AddItem(CreateView):
    form_class = AddProductForm
    template_name = 'products/addpage.html'
    # success_url = reverse_lazy('home') #  Перенаправление после добавления поста
    
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Добавление товара"
        return context

# def addpage(request):
#     if request.method == 'POST':
#         form = AddProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddProductForm()
#     return render(request, 'products/addpage.html', {'form': form, 'title': "Добавление статьи"})


def for_man(request):
    return HttpResponse("Для него")


def for_women(request):
    return HttpResponse("Для неё")


def login(request):
    return HttpResponse("Регистрация")


class ShowItem(DetailView):
    model = Product
    template_name = 'products/item.html'
    slug_url_kwarg = 'item_slug'
    context_object_name = 'products'

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['products'].name
        return context
    
    
# def show_item(request, item_slug):
#     products = get_object_or_404(Product, slug=item_slug)
    
#     context = {
#     'products':products, 
#     'title': 'Категории', 
#     'category_selected': products.category_id,
#     }
    
#     return render(request, 'products/item.html', context=context)


class ShowCatalog(ListView):
    models = Product
    template_name = 'products/index.html'
    context_object_name = 'products'
    allow_empty = False #  404 при отсутсвии записей
    
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Категория: " + str(context['products'][0].category)
        context['category_selected'] = context['products'][0].category_id
        return context

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['cat_slug'], is_available=True)
    

# def show_catalog(request, cat_slug):
#     curr_cat = get_object_or_404(ProductCategory, slug=cat_slug)
#     products = Product.objects.filter(category_id=curr_cat.pk).filter(is_available=True)
    
#     if len(products)==0:
#         raise Http404()
    
#     context = {
#         'products':products, 
#         'title': 'Категории', 
#         'category_selected': curr_cat.pk,
#         }
    
#     return render(request, 'products/index.html', context=context)


def archive(request, year):
    if int(year)>2023:
        # raise Http404()
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам {year}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
