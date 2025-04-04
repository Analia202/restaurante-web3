from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Mesero
from .forms import MeseroForm

class MeseroListView(ListView):
    model = Mesero
    template_name = 'meseros/lista_meseros.html'
    context_object_name = 'meseros'

class MeseroCreateView(CreateView):
    model = Mesero
    form_class = MeseroForm
    template_name = 'meseros/form_meseros.html'
    success_url = reverse_lazy('meseros:lista')

class MeseroUpdateView(UpdateView):
    model = Mesero
    form_class = MeseroForm
    template_name = 'meseros/form_meseros.html'
    success_url = reverse_lazy('meseros:lista')

class MeseroDeleteView(DeleteView):
    model = Mesero
    template_name = 'meseros/confirmar_borrado.html'
    success_url = reverse_lazy('meseros:lista')
