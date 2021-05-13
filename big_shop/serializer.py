from rest_framework import serializers
from .models import Category, Product, Product_photo, Members


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'category_id', "product_slug"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name', 'category_slug', 'category_image', "category_slug"]


class Product_photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_photo
        fields = '__all__'

class Member_photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'