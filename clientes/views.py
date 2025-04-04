from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm

class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/lista_clientes.html'
    context_object_name = 'clientes'

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/form_clientes.html'
    success_url = reverse_lazy('clientes:lista')

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/form_clientes.html'
    success_url = reverse_lazy('clientes:lista')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/confirmar_borrador.html'
    success_url = reverse_lazy('clientes:lista')
