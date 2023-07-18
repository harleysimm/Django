from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ('name', 'description', 'price', 'stock', 'unit', 'largo', 'ancho', 'peso', 'color', 'model')