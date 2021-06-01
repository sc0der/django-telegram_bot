from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import (
    Category, 
    Product, 
    Product_photo, 
    Members,
    CartItem, 
    Cart,
    Order,
    Descriptions
)

# unregister non-used models
admin.site.unregister(User)
admin.site.unregister(Group)

# u=registering models
admin.site.register(Product_photo)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Members)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Descriptions)