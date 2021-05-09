from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .models import Category, Product
from .serializer import ProductSerializer, CategorySerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# api of products

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_new_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"satus":"ok","response": "Новый продукт успешно добавлен"})
    print(serializer.data)
    return Response({"status":"error","response":"Ошибка при добавление нового продукта"})

@api_view(['GET'])
def get_all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response({"products":serializer.data})

@api_view(['GET'])
def get_product_by_id(request, slug):
    product = Product.objects.get(product_slug=slug)
    serializer = ProductSerializer(product)
    return Response({"product":serializer.data})

@api_view(['GET'])
def get_product_by_category_id(request, category_id):
    product = Product.objects.filter(category_id=category_id)
    serializer = ProductSerializer(product, many=True)
    return Response({"category":serializer.data})

# api of categories

@api_view(['GET'])
def get_all_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response({"categories":serializer.data})

@api_view(['GET'])
def get_category_by_id(request, slug):
    category = Category.objects.get(category_slug=slug)
    serializer = CategorySerializer(category)
    return Response({"product":serializer.data})