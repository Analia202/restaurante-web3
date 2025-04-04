from django import forms
from .models import Mesero

class MeseroForm(forms.ModelForm):
    class Meta:
        model = Mesero
        fields = ['nombre', 'apellido', 'telefono']
