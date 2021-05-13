from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import (
    Category, 
    Product,
    Product_photo, 
    Members
)
from .serializer import (
    ProductSerializer, 
    CategorySerializer, 
    Product_photoSerializer, 
    MemberSerializer
)

# api for products

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
    serializer = ProductSerializer(product, many=True, )
    return Response({"category":serializer.data})

@api_view(['GET'])
def get_product_image(request, product_slug):
    product_image = Product_photo.objects.filter(photo_slug = product_slug)
    photo_srzlr = Product_photoSerializer(product_image, many=True)
    return Response({"image: ": photo_srzlr.data})

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

# api of Members

# add new member if not exists
@api_view(['POST'])
def add_new_member(request):
    member = Members.objects.filter(memberID=request.data["memberID"])
    if member.exists():
        return Response(
            {
                "satus":"Registered",
                "response": "Такой участник уже существует"
            }
        )
    else:
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "satus":"isRegistered",
                    "response": "Новый участник успешно добавлен"
                }
            )
    return Response({"status":"error","response":"Ошибка при добавление нового продукта"})


# get  all members
@api_view(['GET'])
def get_members(request):
    members = Members.objects.all()
    serializer = MemberSerializer(members, many=True)
    return Response({"members":serializer.data})

# @api_view(['GET'])
# def get_members(request, userID):
#     members = Members.objects.filter(memberID=userID)
#     if members.exists():
#         return Response({"members":serializer.data})