from django.urls import path

from . import views

urlpatterns = [
    path('recipes', views.recipe_list, name='list'),
    path('recipes/<int:recipe_id>', views.recipe_show, name='show')
]
