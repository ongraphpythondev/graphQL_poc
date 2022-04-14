import graphene
from graphene_django import DjangoObjectType


from .models import Category, Ingredient 

from graphene import relay, ObjectType, String, Schema, List, Field


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category 
        fields = ("id", "name", "ingredients")

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")


class Query(ObjectType):
    all_ingredients = List(IngredientType)
    category_by_name = Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        return Ingredient.objects.select_related("category").all()
    
    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None 


schema = Schema(query=Query)