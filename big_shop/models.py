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
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория")
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