from django import forms
from .models import Pokedex

class PokedexForm(forms.ModelForm):
    class Meta:
        model = Pokedex
        fields = ['name', 'type', 'leyend', 'level', 'image']  # Asegúrate de incluir el campo 'image'
