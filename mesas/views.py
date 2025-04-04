from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Mesa
from .forms import MesaForm

class MesaListView(ListView):
    model = Mesa
    template_name = 'mesas/lista_mesas.html'
    context_object_name = 'mesas'

class MesaCreateView(CreateView):
    model = Mesa
    form_class = MesaForm
    template_name = 'mesas/form_mesa.html'
    success_url = reverse_lazy('mesas:lista')

class MesaUpdateView(UpdateView):
    model = Mesa
    form_class = MesaForm
    template_name = 'mesas/form_mesa.html'
    success_url = reverse_lazy('mesas:lista')

class MesaDeleteView(DeleteView):
    model = Mesa
    template_name = 'mesas/confirmar_borrador.html'
    success_url = reverse_lazy('mesas:lista')
