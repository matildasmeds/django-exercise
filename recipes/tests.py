from django.test import TestCase
import json

RECIPE_SERIALIZATION = {
    "id": 1,
    "name": "Avocado Pasta",
    "description": "Easy and fun",
    "ingredients": [{"name": "Avocado"}, {"name": "Pasta"}],
}


class RecipesListTests(TestCase):

    def test_get_recipes(self):
        """Test GET /api/recipes"""
        url = "/api/recipes"
        res = self.client.get(url, format="json")

        expected = [RECIPE_SERIALIZATION]
        self.assertEquals(json.loads(res.content), expected)
        self.assertEquals(res.status_code, 200)

    def test_get_recipe(self):
        """Test GET /api/recipes/:id"""
        url = "/api/recipes/1"
        res = self.client.get(url, format="json")

        expected = RECIPE_SERIALIZATION
        self.assertEquals(json.loads(res.content), expected)
        self.assertEquals(res.status_code, 200)
