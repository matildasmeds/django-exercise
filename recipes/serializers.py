# {
#    “id”: 1,
#    “name”: “Pizza”
#    “description”: “Put it in the oven”,
#    “ingredients”: [{“name”: “dough”}, {“name”: “cheese”}, {“name”: “tomato”}]
# }

from rest_framework import serializers
from recipes.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description']
