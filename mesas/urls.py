from django.urls import path
from .views import MesaListView, MesaCreateView, MesaUpdateView, MesaDeleteView

app_name = 'mesas'

urlpatterns = [
    path('', MesaListView.as_view(), name='lista'),
    path('nuevo/', MesaCreateView.as_view(), name='nuevo'),
    path('editar/<int:pk>/', MesaUpdateView.as_view(), name='editar'),
    path('eliminar/<int:pk>/', MesaDeleteView.as_view(), name='eliminar'),
]
