# import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Product



class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    category_id = serializers.IntegerField()
    # image = serializers.ImageField(allow_empty_file=True)
    image = serializers.CharField()
    price = serializers.IntegerField()
    quantity = serializers.IntegerField()
    is_available = serializers.BooleanField(default=True)
    description = serializers.CharField()
    short_description = serializers.CharField(max_length=255)
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.image = validated_data.get('image', instance.image)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.is_available = validated_data.get('is_available', instance.is_available)
        instance.description = validated_data.get('description', instance.description)
        instance.short_description = validated_data.get('short_description', instance.short_description)
        instance.save()
        return instance
    

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