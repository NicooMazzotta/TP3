from django.urls import path, include
from inicio import views

app_name = "inicio"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('objetos/', views.Objetos.as_view(), name='objetos'),
    path('objetos/crear/', views.CrearObjeto.as_view(), name='objeto_crear'),
    path('objetos/modificar/<int:pk>/', views.ModificarObjeto.as_view(), name='objeto_modificar'),
    path('objetos/eliminar/<int:pk>/', views.EliminarObjeto.as_view(), name='objeto_eliminar'),
    path('objetos/mostrar/<int:pk>/', views.MostrarObjetos.as_view(), name='objeto_mostrar'),
]
