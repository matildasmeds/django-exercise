from django.test import TestCase
import json


class RecipesListTests(TestCase):
    def test_recipes_list(self):
        """Test GET /api/recipes"""
        url = '/api/recipes'
        res = self.client.get(url, format='json')

        expected = [
            {
                "id": 1,
                "name": "Avocado Pasta",
                "description": "Easy and fun",
                "ingredients": [{"name": "Avocado"}, {"name": "Pasta"}],
            }
        ]
        self.assertEquals(json.loads(res.content), expected)
        self.assertEquals(res.status_code, 200)
