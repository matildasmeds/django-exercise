from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes


@csrf_exempt
@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def recipe_list(request):
    """
    List all recipes, or create new recipe
    """
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=404)


@csrf_exempt
def recipe_show(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
        serializer = RecipeSerializer(recipe)
        return JsonResponse(serializer.data, safe=False)
    except ObjectDoesNotExist:
        raise Http404('Recipe does not exists')
