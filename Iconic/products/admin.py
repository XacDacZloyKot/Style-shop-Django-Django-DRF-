from django.contrib import admin
from .models import *

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 
                    'short_description', 'price', 'image', 'category', 'is_available',
                    'quantity')
    list_display_links = ('name', ) 
    search_fields = ('name', 'short_description', 'price', 'category')
    list_editable = ('description', 'short_description', 'price', 'image', 'quantity', 'is_available')
    list_filter = ('price', 'name', 'is_available', 'quantity')
    prepopulated_fields = {"slug": ('name', )}
    
class ProductcategorysAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name', 'description') 
    search_fields = ('name', 'description')
    prepopulated_fields = {"slug": ('name', )}

admin.site.register(Product, ProductsAdmin)
admin.site.register(ProductCategory, ProductcategorysAdmin)
# admin.site.register(Basket)
