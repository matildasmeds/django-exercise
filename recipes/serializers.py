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
        ingredients = validated_data['ingredients']
        del validated_data['ingredients']
        recipe = Recipe.objects.create(**validated_data)
        recipe.save()

        def save_ingredient(ing_data):
            serializer = IngredientSerializer(data=ing_data)
            if serializer.is_valid():
                Ingredient.objects.create(
                    recipe_id=recipe.id,
                    **serializer.data
                )

        map(save_ingredient, ingredients)
        return recipe
