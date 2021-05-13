from django.conf import settings
from django.conf.urls.static import	static
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from big_shop.views import (
    create_new_product,
    get_all_products, 
    get_product_by_id, 
    get_product_by_category_id,
    get_all_categories, get_category_by_id, get_product_image
)

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('product/add', create_new_product),
    path('product/image/<product_slug>', get_product_image),
    path('product/all', get_all_products),
    path('product/<slug>', get_product_by_id),
    path('category/all', get_all_categories),
    path('category/<slug>', get_category_by_id),
]

urlpatterns	+=	static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)