# {
#    “id”: 1,
#    “name”: “Pizza”
#    “description”: “Put it in the oven”,
#    “ingredients”: [{“name”: “dough”}, {“name”: “cheese”}, {“name”: “tomato”}]
# }

from rest_framework import serializers
from recipes.models import Recipe, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'ingredients']

    # This feels a bit odd, but was the best I could do
    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')
        recipe = Recipe(**validated_data)
        recipe.save()

        for ing_data in ingredients:
            serializer = IngredientSerializer(data=ing_data)
            if serializer.is_valid():
                ingredient = Ingredient(
                    recipe=recipe,
                    **serializer.data
                )
                ingredient.save()
                recipe.ingredients.add(ingredient)

        return recipe
