from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)