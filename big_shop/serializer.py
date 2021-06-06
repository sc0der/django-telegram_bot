from rest_framework import serializers
from .models import (
    Category, 
    Product, 
    Product_photo, 
    Members,
    Cart, 
    CartItem, 
    Order,
    Descriptions
)

# Сериализаторы 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class Product_photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_photo
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



class DescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descriptions
        fields = '__all__'