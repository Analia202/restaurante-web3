from django.urls import path
from .views import MeseroListView, MeseroCreateView, MeseroUpdateView, MeseroDeleteView

app_name = 'meseros'

urlpatterns = [
    path('', MeseroListView.as_view(), name='lista'),
    path('nuevo/', MeseroCreateView.as_view(), name='nuevo'),
    path('editar/<int:pk>/', MeseroUpdateView.as_view(), name='editar'),
    path('eliminar/<int:pk>/', MeseroDeleteView.as_view(), name='eliminar'),
]
