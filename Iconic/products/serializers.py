# import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Product, ProductCategory



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "description", "short_description", "price", "image", "category", "is_available", "slug")
    
    
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"
# region <Create custom serializer>
# def encode():
#     model = ProductModel('bebra', 2, "C:\\Users\\treen\\Downloads\\aga.jpg", 1500, 300, True, 'Крутой мужик - мощный', "А ты хорош")
#     model_sr = ProductSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr._data)
#     print(json)
    
    
# def decode():
#     stream = io.BytesIO(b'"name":"Govno","category_id":4,"image":"asd","price":1500,"quantity":500,"is_available":true,"description":"PPC","short_description":"ZXC"')
#     data = JSONParser().parse(stream)
#     serializers = ProductSerializer(data=data)
#     print(serializers.is_valid())
#     print(serializers.validated_data)
    
# class ProductModel:
#     def __init__(self, name, category_id, image, price, quantity, is_available, description, short_description):
#         self.name = name
#         self.category_id = category_id
#         self.image = image
#         self.price = price
#         self.quantity = quantity
#         self.is_available = is_available
#         self.description = description
#         self.short_description = short_description
#endregion

