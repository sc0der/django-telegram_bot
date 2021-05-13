# Generated by Django 3.1.6 on 2021-05-13 06:02

import big_shop.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='Категория')),
                ('category_slug', models.SlugField(default='', editable=False)),
                ('category_image', models.ImageField(upload_to='photo_archive/category/')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='Продукт')),
                ('price', models.FloatField(default=1.0, verbose_name='Цена')),
                ('created_date', models.DateField(auto_now=True, verbose_name='Дата')),
                ('product_slug', models.SlugField(default='', editable=False)),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='big_shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Product_photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=big_shop.models.Product_photo.product_photo_location)),
                ('photo_slug', models.SlugField(default='', editable=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='big_shop.product')),
            ],
            options={
                'verbose_name': 'Фотография продукта',
                'verbose_name_plural': 'Фотографии продуктов',
            },
        ),
    ]
