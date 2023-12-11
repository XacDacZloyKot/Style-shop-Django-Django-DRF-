from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound
from .models import *
from .forms import *


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'products':products, 
        'title': 'Каталог', 
        'category_selected': 0,
        }
    
    return render(request, 'products/index.html', context=context)

def about(request):
    return render(request, 'products/about.html', {'title': 'О сайте'})

def addpage(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddProductForm()
    return render(request, 'products/addpage.html', {'form': form, 'title': "Добавление статьи"})

def for_man(request):
    return HttpResponse("Для него")

def for_women(request):
    return HttpResponse("Для неё")

def login(request):
    return HttpResponse("Регистрация")

def show_item(request, item_slug):
    products = get_object_or_404(Product, slug=item_slug)
    
    context = {
    'products':products, 
    'title': 'Категории', 
    'category_selected': products.category_id,
    }
    
    return render(request, 'products/item.html', context=context)

def show_catalog(request, cat_slug):
    curr_cat = get_object_or_404(ProductCategory, slug=cat_slug)
    products = Product.objects.filter(category_id=curr_cat.pk)
    
    if len(products)==0:
        raise Http404()
    
    context = {
        'products':products, 
        'title': 'Категории', 
        'category_selected': curr_cat.pk,
        }
    
    return render(request, 'products/index.html', context=context)

def archive(request, year):
    if int(year)>2023:
        # raise Http404()
        return redirect('home', permanent=True)
        
    return HttpResponse(f"<h1>Архив по годам {year}</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
