from django.urls import path
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView

app_name = 'clientes'

urlpatterns = [
    path('', ClienteListView.as_view(), name='lista'),
    path('nuevo/', ClienteCreateView.as_view(), name='nuevo'),
    path('editar/<int:pk>/', ClienteUpdateView.as_view(), name='editar'),
    path('eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='eliminar'),
]
