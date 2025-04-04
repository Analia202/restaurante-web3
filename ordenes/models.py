from django.db import models
from clientes.models import Cliente
from platos.models import Plato
from mesas.models import Mesa
from meseros.models import Mesero

class Orden(models.Model):
    ESTADO_CHOICES = (
        ('abierta', 'Abierta'),
        ('cerrada', 'Cerrada'),
    )

    platos = models.ManyToManyField(Plato)
    mesero = models.ForeignKey(Mesero, on_delete=models.SET_NULL, null=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='abierta')
    fechaHora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orden #{self.id} - {self.estado}"
