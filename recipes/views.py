from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.renderers import JSONRenderer


class RecipeViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    GenericViewSet):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    renderer_classes = [JSONRenderer]
