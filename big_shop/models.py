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

def get_category_image_path(instance, filename, value):
  return os.path.join("photo_archive/category/", value)

def get_product_image_path(instance, filename):
  return os.path.join("photo_archive/products/", slug_generator()+".png")

class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name="Категория")
    category_slug = models.SlugField(
        default='',
        editable=False,
    )
    category_image = models.ImageField(upload_to="photo_archive/category/")
    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.category_name
        }
        return reverse('category-pk-category_name-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.category_name
        self.category_slug = translate_slug(value)
        super().save(*args, **kwargs)

    def get_image_url(self):
        return str(self.category_image)

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
    image = models.ImageField(upload_to=get_product_image_path)
    product_slug = models.SlugField(
        default='',
        editable=False,
    )

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.product_name
        }
        return reverse('product-pk-product_name-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.product_name
        self.product_slug = slugify(slug_generator())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = ('Продукт')
        verbose_name_plural = ('Продукты')