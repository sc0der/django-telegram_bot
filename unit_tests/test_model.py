from django.test import TestCase
from big_shop.models import Category

# Create your tests here.
class CategoryTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(category_name='Компьютеры')

    def test_category_name(self):
        print("----- testing category name -----")
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('category_name').verbose_name
        self.assertEquals(field_label,'Категория')