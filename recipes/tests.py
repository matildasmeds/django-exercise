from django.test import TestCase
from rest_framework.test import APIClient
from recipes.models import Recipe, Ingredient
from django.core.exceptions import ObjectDoesNotExist

import json

RECIPE_DICT = {
    # Created with a data migration, would probably be better as a fixture
    # or created inside the test
    'pasta': {
        "id": 1,
        "name": "Avocado Pasta",
        "description": "Easy and fun",
        "ingredients": [{"name": "Avocado"}, {"name": "Pasta"}],
    },
    'pizza': {
        "name": "Pizza",
        "description": "Put it in the oven",
        "ingredients": [
            {"name": "dough"},
            {"name": "cheese"},
            {"name": "tomato"}],
    }
}


class RecipeAPITests(TestCase):
    def test_get_recipes(self):
        """Test GET /api/recipe"""
        url = "/api/recipe/"
        self.client = APIClient()
        res = self.client.get(url, format="json")

        expected = [RECIPE_DICT['pasta']]
        self.assertEquals(json.loads(res.content), expected)
        self.assertEquals(res.status_code, 200)

    def test_post_recipes(self):
        """Test POST /api/recipe"""
        url = "/api/recipe/"
        params = RECIPE_DICT['pizza']
        res = self.client.post(
            url,
            json.dumps(params),
            content_type='application/json'
        )

        payload = json.loads(res.content)
        id = payload.pop('id')
        self.assertEquals(id, 2)
        self.assertEquals(payload, params)
        self.assertEquals(res.status_code, 201)

    def test_get_recipe(self):
        """Test GET /api/recipe/:id"""
        url = "/api/recipe/1/"
        res = self.client.get(url, format="json")

        expected = RECIPE_DICT['pasta']
        self.assertEquals(json.loads(res.content), expected)
        self.assertEquals(res.status_code, 200)

    def test_search_recipe(self):
        """Test GET /api/recipe/?name=<search string>"""
        url = '/api/recipe/?name=Pi'
        res = self.client.get(url, format='json')

        expected = [RECIPE_DICT['pizza']]
        self.assertEquals(json.loads(res.content), expected)
        self.assertEquals(res.status_code, 200)

    def test_update_recipe(self):
        """Test PATCH /api/recipe/:id"""
        url = "/api/recipe/1/"
        params = {
          'name': 'Pizza',
          'description': 'Put it in the oven',
          'ingredients': [{'name': 'casa-tarradellas'}]
        }
        res = self.client.patch(url,
                                json.dumps(params),
                                content_type='application/json')

        payload = json.loads(res.content)
        params['id'] = 1

        self.assertEquals(res.status_code, 200)
        self.assertEquals(payload, params)

    def assert_object_does_not_exist(self, model, id):
        with self.assertRaises(ObjectDoesNotExist):
            model.objects.get(pk=id)

    # These tests can't be run in parallel atm
    def test_delete_recipe(self):
        """Test DELETE /api/recipe/:id"""
        url = "/api/recipe/1/"
        recipe_id = 1
        recipe = Recipe.objects.get(pk=recipe_id)
        ingredient_ids = [ing.id for ing in recipe.ingredients.all()]

        res = self.client.delete(url)

        self.assertEquals(res.status_code, 204)
        self.assert_object_does_not_exist(Recipe, 1)
        for id in ingredient_ids:
            self.assert_object_does_not_exist(Ingredient, id)
