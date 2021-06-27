
from shop_telegram_bot import charts
from shop_telegram_bot import counters
from django.conf import settings
from django.apps import apps
from vali.views import ValiDashboardBase
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
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
from .serializer import (
    ProductSerializer, 
    CategorySerializer, 
    Product_photoSerializer, 
    MemberSerializer, 
    CartItemSerializer, 
    CartSerializer, 
    OrderSerializer,
    DescriptionsSerializer
)


class ValiDashboardView(ValiDashboardBase):
    template_name = 'dashboard.html'
    users = (apps.get_model(settings.AUTH_USER_MODEL)).objects.count()
    groups = Product.objects.count()
    apps_len = len(apps.get_models())
    list_charts = [
        {
            # Support Chart types: Bar, Line, Radar
            "name": "asdasd",
            "title": "asdasd",
            "chart_type": "Bar",
            "labels": ["2018-03-01", "2018-03-02", "2018-03-03", "2018-03-04", "2018-03-05"],
            "datasets": [
                {
                    "label": "dataset 1",
                    "fillColor": "rgba(220,220,220,0.2)",
                    "strokeColor": "rgba(220,220,220,1)",
                    "pointColor": "rgba(220,220,220,1)",
                    "pointStrokeColor": "#fff",
                    "pointHighlightFill": "#fff",
                    "pointHighlightStroke": "rgba(220,220,220,1)",
                    "data": [65, 59, 80, 81, 80]
                },
                {
                    "label": "dataset 2",
                    "fillColor": "rgba(151,187,205,0.2)",
                    "strokeColor": "rgba(151,187,205,1)",
                    "pointColor": "rgba(151,187,205,1)",
                    "pointStrokeColor": "#fff",
                    "pointHighlightFill": "#fff",
                    "pointHighlightStroke": "rgba(151,187,205,1)",
                    "data": [28, 48, 40, 19, 69]
                }
            ],
        },
        {
            # Support Chart types: PolarArea, Pie, Doughnut
            "name": "piechart1",
            "title": "Piechart",
            "chart_type": "Pie",
            "datasets": [
                {
                    "value": 300,
                    "color": "#F7464A",
                    "highlight": "#FF5A5E",
                    "label": "Red"
                },
                {
                    "value": 50,
                    "color": "#46BFBD",
                    "highlight": "#5AD3D1",
                    "label": "Green"
                },
                {
                    "value": 100,
                    "color": "#FDB45C",
                    "highlight": "#FFC870",
                    "label": "Yellow"
                },
            ]
        }
    ]

    # default icons data
    list_counters = [
        {"title": "Users", "value": users, "style": "primary", "icon": "fa-user-circle"},
        {"title": "Groups", "value": groups, "style": "warning", "icon": "fa-users"},
        {"title": "Apps", "value": apps_len, "style": "info", "icon": "fa-briefcase"},
        {"title": "Charts", "value": len(list_charts), "style": "danger", "icon": "fa-line-chart"},
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

@api_view(['GET'])
def get_All_descr(request):
    order = Descriptions.objects.all()
    serlzr = DescriptionsSerializer(order, many=True)
    return Response({"messages": serlzr.data})


@api_view(['GET', 'POST'])
def get_descr_by_name(request):
    value = request.data['slug']
    order = Descriptions.objects.filter(slug=value)
    serlzr = DescriptionsSerializer(order, many=True)
    return Response({"messages": serlzr.data})