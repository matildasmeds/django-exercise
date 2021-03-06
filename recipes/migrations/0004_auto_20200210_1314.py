# Generated by Django 2.2.10 on 2020-02-10 13:14

from django.db import migrations


def seed_recipe(apps, _):
    Recipe = apps.get_model('recipes', 'Recipe')
    Ingredient = apps.get_model('recipes', 'Ingredient')

    recipe = Recipe(
        name='Avocado Pasta',
        description='Easy and fun',
    )
    recipe.save()
    Ingredient(name='Avocado', recipe_id=recipe.id).save()
    Ingredient(name='Pasta', recipe_id=recipe.id).save()


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20200210_1103'),
    ]

    operations = [
        migrations.RunPython(seed_recipe)
    ]
