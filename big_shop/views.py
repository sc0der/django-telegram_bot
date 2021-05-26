
from shop_telegram_bot import charts
from shop_telegram_bot import counters
from vali.views import ValiDashboardBase
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import (
    Category, 
    Product,
    Product_photo, 
    Members, Cart, CartItem, Order
)
from .serializer import (
    ProductSerializer, 
    CategorySerializer, 
    Product_photoSerializer, 
    MemberSerializer, 
    CartItemSerializer, 
    CartSerializer, 
    OrderSerializer
)


class ModelDashboardView(ValiDashboardBase):
    template_name = 'dashboard.html'

    list_counters = [
        counters.MyModelCounter(),
    ]   
    list_charts = [
        charts.ChartCounter(),
    ]

# api for products

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_new_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"satus":"OK","response": "Новый продукт успешно добавлен"})
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
    return Response(serializer.data)

@api_view(['GET'])
def get_product_by_category_id(request, category_slug):
    category = Category.objects.filter(category_slug = category_slug)
    for product in category:
        product_list = product.products.all()
        serializer = ProductSerializer(product_list, many=True)
    return Response({"products_by_category":serializer.data})

@api_view(['GET'])
def get_product_image(request, product_slug):
    product_image = Product_photo.objects.filter(photo_slug = product_slug)
    photo_srzlr = Product_photoSerializer(product_image, many=True)
    return Response({"images": photo_srzlr.data})

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
    return Response(serializer.data)

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
        
    return Response(
        {
            "status":"error",
            "response":serializer.data
        }
    )

# get  all members
@api_view(['GET'])
def get_members(request):
    members = Members.objects.all()
    serializer = MemberSerializer(members, many=True)
    return Response({"members":serializer.data})


# Работа с заказамы и корзинам
@api_view(['POST'])
def post_cart_item(request):
    # print(request.data)
    # product_id = request.data['product']
    cart = CartItem.objects.get(id=1)
    print(cart.cart_set.all())
    serlzr = CartItemSerializer(data=request.data)
    if serlzr.is_valid():
        serlzr.save()
        return Response(
            {
                "status": "OK",
                "message": "Успешно добавлен"
            }
        )
    return Response({"error": "Не удалос добавить в корзину"})

@api_view(['GET'])
def get_cart_item(request, cItem_id):
    cartItem = CartItem.objects.get(id=cItem_id)
    serlzr = CartItemSerializer(cartItem)
    return Response({"cart_item": serlzr.data})

@api_view(['POST'])
def post_cart(request):
    serlzr = CartSerializer(data=request.data)
    if serlzr.is_valid():
        serlzr.save()
        return Response(
            {
                "status": "OK",
                "message": "Успешно добавлен"
            }
        )
    return Response({"error": "Не удалось добавить"})

@api_view(['GET'])
def get_carts(request):
    cart = Cart.objects.all()
    serlzr = CartSerializer(cart, many=True)
    return Response({"cart": serlzr.data})

@api_view(['POST'])
def post_order(request):
    serlzr = OrderSerializer(data=request.data)
    if serlzr.is_valid():
        serlzr.save()
        return Response(
            {
                "status": "OK",
                "message": "Ваш заказ успешно отправлен"
            }
        )
    return Response({"error": "Не удалось отправить"})

@api_view(['GET'])
def get_order_item(request):
    order = Order.objects.all()
    serlzr = OrderSerializer(order, many=True)
    return Response({"order": serlzr.data})

