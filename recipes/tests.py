from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

import json

RECIPE_SERIALIZATION = {
    "id": 1,
    "name": "Avocado Pasta",
    "description": "Easy and fun",
    "ingredients": [{"name": "Avocado"}, {"name": "Pasta"}],
}


class RecipeListTests(TestCase):
    def test_get_recipes(self):
        """Test GET /api/recipe"""
        url = "/api/recipe"
        self.client = APIClient()
        res = self.client.get(url, format="json")
        print(res)

        expected = [RECIPE_SERIALIZATION]
        self.assertEquals(json.loads(res.content), expected)
        self.assertEquals(res.status_code, 200)

    def test_post_recipes(self):
        """Test POST /api/recipe"""
        url = "/api/recipe"
        params = {
            "name": "Pizza",
            "description": "Put it in the oven",
            "ingredients": [
                {"name": "dough"},
                {"name": "cheese"},
                {"name": "tomato"}],
        }
        res = self.client.post(
            url,
            json.dumps(params),
            content_type='application/json'
        )
        print(res)

        payload = json.loads(res.content)
        params['id'] = payload['id']
        self.assertEquals(payload, params)
        self.assertEquals(res.status_code, 201)


class RecipeShowTests(TestCase):
    def test_get_recipe(self):
        """Test GET /api/recipe/:id"""
        url = "/api/recipe/1"
        res = self.client.get(url, format="json")
        print(res)

        expected = RECIPE_SERIALIZATION
        self.assertEquals(json.loads(res.content), expected)
        self.assertEquals(res.status_code, 200)
