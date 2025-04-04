from django.urls import path
from .views import OrdenListView, OrdenCreateView, OrdenUpdateView, OrdenDeleteView, seleccionar_cliente, asignar_cliente_y_cerrar, TodasLasOrdenesView

app_name = 'ordenes'

urlpatterns = [
    path('', OrdenListView.as_view(), name='lista'),
    path('nuevo/', OrdenCreateView.as_view(), name='nuevo'),
    path('editar/<int:pk>/', OrdenUpdateView.as_view(), name='editar'),
    path('eliminar/<int:pk>/', OrdenDeleteView.as_view(), name='eliminar'),
    path('seleccionar-cliente/<int:orden_id>/', seleccionar_cliente, name='seleccionar_cliente'),
    path('asignar-cliente/<int:orden_id>/<int:cliente_id>/', asignar_cliente_y_cerrar, name='asignar_cliente_y_cerrar'),
    path('todas/', TodasLasOrdenesView.as_view(), name='todas_las_ordenes'),

]
