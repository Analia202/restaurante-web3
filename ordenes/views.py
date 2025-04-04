from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Orden
from .forms import OrdenForm
from clientes.models import Cliente


class OrdenListView(ListView):
    model = Orden
    template_name = 'ordenes/lista_ordenes.html'
    context_object_name = 'ordenes'

# ➕ Crear orden
class OrdenCreateView(CreateView):
    model = Orden
    form_class = OrdenForm
    template_name = 'ordenes/form_orden.html'
    success_url = reverse_lazy('ordenes:lista')

class OrdenUpdateView(UpdateView):
    model = Orden
    form_class = OrdenForm
    template_name = 'ordenes/form_orden.html'
    success_url = reverse_lazy('ordenes:lista')

    def dispatch(self, request, *args, **kwargs):
        orden = self.get_object()
        if orden.estado == 'cerrada':
            messages.warning(request, f"La orden #{orden.id} ya está cerrada y no puede ser editada.")
            return redirect('ordenes:lista')
        return super().dispatch(request, *args, **kwargs)


class OrdenDeleteView(DeleteView):
    model = Orden
    template_name = 'ordenes/confirmar_borrado.html'
    success_url = reverse_lazy('ordenes:lista')


def seleccionar_cliente(request, orden_id):
    clientes = Cliente.objects.all()
    return render(request, 'ordenes/seleccionar_cliente.html', {
        'clientes': clientes,
        'orden_id': orden_id
    })


def asignar_cliente_y_cerrar(request, orden_id, cliente_id):
    orden = get_object_or_404(Orden, id=orden_id)
    cliente = get_object_or_404(Cliente, id=cliente_id)

    orden.cliente = cliente
    orden.estado = 'cerrada'
    orden.save()

    messages.success(request, f"La orden #{orden.id} fue pagada y asignada a {cliente.nombre}.")
    return redirect('ordenes:todas_las_ordenes')

class TodasLasOrdenesView(ListView):
    model = Orden
    template_name = 'ordenes/todas_las_ordenes.html'
    context_object_name = 'ordenes'
