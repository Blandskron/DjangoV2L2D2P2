from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostar_pokemon, name='pokemon_list'),
    path('create/', views.crear_pokemon, name='pokemon_create'),
    path('edit/<int:pk>/', views.crear_pokemon, name='pokemon_update'),
    path('delete/<int:pk>/', views.eliminar_pokemon, name='pokemon_delete'),
    path('pokemon/<int:pk>/', views.pokedex_detail, name='pokedex_detail'),
] 
