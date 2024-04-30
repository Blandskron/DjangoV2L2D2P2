from django.shortcuts import render, redirect
from .models import Pokedex
from .forms import PokedexForm

def mostar_pokemon(request):
    pokemons = Pokedex.objects.all()
    return render(request, 'apipokemon/pokemon.html', {'pokemons': pokemons})


def pokedex_detail(request, pk):
    pokemon = Pokedex.objects.get(pk=pk)
    return render(request, 'apipokemon/pokedex_detail.html', {'pokemon': pokemon})


def crear_pokemon(request):
    if request.method == 'POST':
        form = PokedexForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokemon_list')
    else:
        form = PokedexForm()
    return render(request, 'apipokemon/agregar_pokemon.html', {'form': form})

def actualizar_pokemon(request, pk):
    pokemon = Pokedex.objects.get(pk=pk)
    if request.method == 'POST':
        form = PokedexForm(request.POST, request.FILES, instance=pokemon)  
        if form.is_valid():
            form.save()
            return redirect('pokemon_list')
    else:
        form = PokedexForm(instance=pokemon)
    return render(request, 'apipokemon/agregar_pokemon.html', {'form': form})


def eliminar_pokemon(request, pk):
    pokemon = Pokedex.objects.get(pk=pk)
    if request.method == 'POST':
        pokemon.delete()
        return redirect('pokemon_list')
    return render(request, 'apipokemon/pokemon_confirm_delete.html', {'pokemon': pokemon})
