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

    def add_ingredients(self, recipe, ingredients):
        for ing_data in ingredients:
            serializer = IngredientSerializer(data=ing_data)
            if serializer.is_valid():
                Ingredient.objects.create(
                    recipe=recipe,
                    **serializer.data
                )

    # This feels a bit odd, but was the best I could do
    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')
        recipe = Recipe(**validated_data)
        recipe.save()

        self.add_ingredients(recipe, ingredients)

        return recipe

    def update(self, recipe, validated_data):
        recipe.name = validated_data.get('name', recipe.name)
        recipe.description = validated_data.get('description',
                                                recipe.description)
        ingredients = validated_data.pop('ingredients')

        recipe.ingredients.all().delete()
        self.add_ingredients(recipe, ingredients)
        recipe.save()

        return recipe
