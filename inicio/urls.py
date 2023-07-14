from django.urls import path, include
from inicio import views

app_name = "inicio"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('objetos/', views.objetos, name='objetos'),
    path('objetos/vendedor', views.ListarObjetos.as_view(), name='objetos_vendedor'),
    path('objetos/vendedor/crear/', views.CrearObjeto.as_view(), name='objeto_crear'),
    path('objetos/comprador', views.ListarObjetosDisponibles.as_view(), name='objetos_comprador'),
    path('objetos/comprador/comprar/<int:objeto_id>/', views.confirmar_compra, name='objeto_confirmar_compra'),
    path('objetos/historial_comprados', views.ListarObjetosComprados.as_view(), name='objetos_historial_comprados'),
    path('objetos/historial_vendidos', views.ListarObjetosVendidos.as_view(), name='objetos_historial_vendidos'),
    path('objetos/modificar/<int:pk>/', views.ModificarObjeto.as_view(), name='objeto_modificar'),
    path('objetos/eliminar/<int:pk>/', views.EliminarObjeto.as_view(), name='objeto_eliminar'),
    path('objetos/mostrar/<int:pk>/', views.MostrarObjetos.as_view(), name='objeto_mostrar'),
    

]
