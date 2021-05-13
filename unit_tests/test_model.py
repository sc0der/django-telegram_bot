from django.test import TestCase
from big_shop.models import Category, Members

class CategoryTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(category_name='Компьютеры')

    def test_category_name(self):
        print("----- testing category name -----")
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('category_name').verbose_name
        self.assertEquals(field_label,'Категория')

class MemberTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        Members.objects.create(memberID='123456789')

    def test_members(self):
        print("----- testing members -----")
        member = Members.objects.get(id=1)
        field_label = member._meta.get_field('memberID').verbose_name
        field_label2 = member._meta.get_field('mName').verbose_name
        self.assertEquals(field_label,'ID-участника')
        self.assertEquals(field_label2,'USERNAME-участника')