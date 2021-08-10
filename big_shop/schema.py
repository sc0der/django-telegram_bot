
from django.db.models import fields, query
import graphene
from graphene_django import DjangoObjectType
from .models import Category

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'category_slug', 'excerpt')

class Query(graphene.ObjectType):
    all_category = graphene.List(CategoryType)
    def resolve_all_category(root, info):
        return Category.objects.all()

schema = graphene.Schema(query = Query)