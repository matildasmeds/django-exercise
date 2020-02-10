from django.test import TestCase
from rest_framework import status

import json

RECIPE_SERIALIZATION = {
    "id": 1,
    "name": "Avocado Pasta",
    "description": "Easy and fun",
    "ingredients": [{"name": "Avocado"}, {"name": "Pasta"}],
}


class RecipeListTests(TestCase):

    def test_get_recipes(self):
        """Test GET /api/recipes"""
        url = "/api/recipes"
        res = self.client.get(url, format="json")

        expected = [RECIPE_SERIALIZATION]
        self.assertEquals(json.loads(res.content), expected)
        self.assertEquals(res.status_code, 200)

    def test_post_recipes(self):
        """Test POST /api/recipes"""
        url = "/api/recipes"
        params = {
            'name': 'Sliced avocado',
            'description': 'Cut a ripe avocado in half, and cut into slices',
        }
        res = self.client.post(url, params)

        self.assertEquals(res.status_code, 201)
        self.assertContains(res, 'id')


class RecipeShowTests(TestCase):

    def test_get_recipe(self):
        """Test GET /api/recipes/:id"""
        url = "/api/recipes/1"
        res = self.client.get(url, format="json")

        expected = RECIPE_SERIALIZATION
        self.assertEquals(json.loads(res.content), expected)
        self.assertEquals(res.status_code, 200)
