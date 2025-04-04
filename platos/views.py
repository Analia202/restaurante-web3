from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Plato
from .forms import PlatoForm

class PlatoListView(ListView):
    model = Plato
    template_name = 'platos/lista_platos.html'
    context_object_name = 'platos'

class PlatoCreateView(CreateView):
    model = Plato
    form_class = PlatoForm
    template_name = 'platos/form_plato.html'
    success_url = reverse_lazy('platos:lista')

class PlatoUpdateView(UpdateView):
    model = Plato
    form_class = PlatoForm
    template_name = 'platos/form_plato.html'
    success_url = reverse_lazy('platos:lista')

class PlatoDeleteView(DeleteView):
    model = Plato
    template_name = 'platos/confirmar_borrado.html'
    success_url = reverse_lazy('platos:lista')
