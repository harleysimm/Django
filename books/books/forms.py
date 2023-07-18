from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    type = forms.CharField(widget=forms.RadioSelect(choices=Book.TIPOS_BOOK))
    preferencia = forms.CharField(widget=forms.CheckboxSelectMultiple(choices=Book.COLOR_FAVORITO))
    class Meta:
        model = Book
        fields = ('titulo', 'editorial', 'state', 'type', 'preferencia')