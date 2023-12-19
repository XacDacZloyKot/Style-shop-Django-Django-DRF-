# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.category, filename)


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name="Название", db_index=True)
    description = models.CharField(blank=True, null=True, verbose_name="Описание", max_length=64)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Категория" 
        verbose_name_plural = "Категории" 
        ordering = ['id', ]


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name="Товар")
    description = models.TextField(blank=True, verbose_name="Описание")
    short_description = models.CharField(max_length=64, verbose_name="Краткое описание")
    price = models.DecimalField(decimal_places=2, max_digits=8, verbose_name="Цена")
    image = models.ImageField(upload_to=user_directory_path, verbose_name="Изображение", blank=True)
    category = models.ForeignKey(to=ProductCategory, verbose_name=("Категория"), on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=1)
    is_available = models.BooleanField(verbose_name="В наличии", default=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    
    
    def __str__(self) -> str:
        return self.name
    
    
    def get_absolute_url(self):
        return reverse('item', kwargs={'item_slug': self.slug})
    
    class Meta:
        verbose_name = "Товар" 
        verbose_name_plural = "Товары" 
        ordering = ['name', 'category']
        
        
    
    
class Basket(models.Model):
    created = models.DateTimeField(auto_now_add=True) 
    product = models.ManyToManyField(Product, verbose_name="Товар")
    
    class Meta:
        verbose_name = "Корзина пользователя"
        verbose_name_plural = "Корзины пользователей" 
        
    