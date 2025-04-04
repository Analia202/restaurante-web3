from django.urls import path
from .views import PlatoListView, PlatoCreateView, PlatoUpdateView, PlatoDeleteView

app_name = 'platos'

urlpatterns = [
    path('', PlatoListView.as_view(), name='lista'),
    path('nuevo/', PlatoCreateView.as_view(), name='nuevo'),
    path('editar/<int:pk>/', PlatoUpdateView.as_view(), name='editar'),
    path('eliminar/<int:pk>/', PlatoDeleteView.as_view(), name='eliminar'),
]
