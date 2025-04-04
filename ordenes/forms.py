from django import forms
from .models import Orden
from django.core.exceptions import ValidationError

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['platos', 'mesero', 'mesa', 'estado']  # ❌ SIN 'fechaHora'
        widgets = {
            'platos': forms.CheckboxSelectMultiple
        }

    def clean(self):
        cleaned_data = super().clean()
        mesa = cleaned_data.get('mesa')
        cliente = cleaned_data.get('cliente')
        instance_id = self.instance.id  # para excluirse a sí misma si es edición

        # Validar que la mesa no esté ocupada
        if mesa:
            if Orden.objects.filter(mesa=mesa, estado='abierta').exclude(id=instance_id).exists():
                raise ValidationError(f"La mesa {mesa.numero} ya está ocupada por otra orden abierta.")

        # Validar que el cliente no tenga una orden abierta
        if cliente:
            if Orden.objects.filter(cliente=cliente, estado='abierta').exclude(id=instance_id).exists():
                raise ValidationError(f"El cliente {cliente.nombre} ya tiene una orden abierta.")

        return cleaned_data
