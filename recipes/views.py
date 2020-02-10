from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer


@csrf_exempt
def recipe_list(request):
    """
    List all recipes, or create new recipe
    """
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse(serializer.data, safe=False)
