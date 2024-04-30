from django import forms
from .models import Productos

class Inventarios(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'descripcion', 'cantidad']
        