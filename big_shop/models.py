from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from pytils.translit import slugify as translate_slug
from django.utils.crypto import get_random_string
import string
import uuid
import os

def slug_generator():
  code = get_random_string(30, allowed_chars=string.ascii_uppercase + string.digits)
  return code



class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name="Категория")
    category_slug = models.SlugField(
        default='',
        editable=False,
    )
    category_image = models.ImageField(upload_to="photo_archive/category/")

    def save(self, *args, **kwargs):
        value = self.category_name
        self.category_slug = translate_slug(value)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = ('Категория')
        verbose_name_plural = ('Категории')

class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name="Продукт")
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="products", null=True, verbose_name="Категория")
    price = models.FloatField(default=1.0, verbose_name="Цена")
    created_date = models.DateField(auto_now=True, verbose_name="Дата")
    product_slug = models.SlugField(
        default='',
        editable=False,
    )

    def save(self, *args, **kwargs):
        self.product_slug = slugify(slug_generator())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name
        
    class Meta:
        verbose_name = ('Продукт')
        verbose_name_plural = ('Продукты')

class Product_photo(models.Model):
    def product_photo_location(self, filename):
        return 'photo_archive/products/{}'.format(self.product.product_slug+".png")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=product_photo_location)
    photo_slug = models.SlugField(
        default='',
        editable=False,
    )

    def __str__(self):
        return self.product.product_name

    def save(self, *args, **kwargs):
        self.photo_slug = self.product.product_slug
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = ('Фотография продукта')
        verbose_name_plural = ('Фотографии продуктов')

class Members(models.Model):
    memberID = models.CharField(max_length=150, verbose_name="ID-участника")
    mName = models.CharField(max_length=50, verbose_name="USERNAME-участника")
    # banned = models.BooleanField(default=False, verbose_name="Участник забанен")

    def __str__(self):
        return self.mName

    class Meta:
        verbose_name = ('Участник')
        verbose_name_plural = ('Участники')

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null=True)
    qty = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __unicode__(self):
        return "cart item for product {0}".format(self.product.product_name)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = ('Запрос')
        verbose_name_plural = ('Запросы')

class Cart(models.Model):
    items = models.ManyToManyField(CartItem)
    item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    
    def __unicode__(self):
        return str(self.id)

    class Meta:
        verbose_name = ('Корзина')
        verbose_name_plural = ('Корзина')


class Order(models.Model):
    order = models.CharField(max_length=100)
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.order = self.cart.product.product_name
        super().save(*args, **kwargs)