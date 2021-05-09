from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Category, Product

# unregister non-used models
admin.site.unregister(User)
admin.site.unregister(Group)

# u=registering models
admin.site.register(Category)
admin.site.register(Product)