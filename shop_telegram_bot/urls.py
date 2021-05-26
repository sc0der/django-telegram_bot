from django.conf import settings
from django.conf.urls.static import	static
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from big_shop.views import (
    create_new_product,
    get_all_products,
    get_carts, 
    get_product_by_id, 
    get_product_by_category_id,
    get_all_categories, 
    get_category_by_id, 
    get_product_image,
    add_new_member, 
    get_members, 
    get_cart_item,
    get_order_item,
    get_carts,
    post_cart,
    post_cart_item,
    post_order
)

router = routers.DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('vali/', include('vali.urls')),
    path('product/add', create_new_product),
    path('product/image/<product_slug>', get_product_image),
    path('product/all', get_all_products),
    path('product/<slug>', get_product_by_id),
    path('category/all', get_all_categories),
    path('category/<slug>', get_category_by_id),
    path('products/category/<category_slug>', get_product_by_category_id),
    path('member/add', add_new_member),
    path('member/all', get_members),
    path('order/add', post_order),
    path('order/all', get_order_item),
    path('cart/add', post_cart),
    path('cart/all', get_carts),
    path('cart_item/add', post_cart_item),
    path('cart_item/<cItem_id>', get_cart_item),

]

urlpatterns	+=	static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)