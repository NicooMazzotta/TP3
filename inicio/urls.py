from django.urls import path, include
from inicio import views

app_name = "inicio"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('comprador/', views.comprador, name='comprador'),
    path('comprador/crear', views.comprador_crear, name='comprador/crear'),
    path('comprador/acceder', views.comprador_acceder, name='comprador/acceder'),
    path('vendedor/', views.vendedor, name='vendedor'),
    path('vendedor/crear', views.vendedor_crear, name='vendedor/crear'),
    path('vendedor/acceder', views.vendedor_acceder, name='vendedor/acceder'),
    path('objetos', views.objetos, name='objetos'),
    path('objeto_crear', views.objeto_crear, name='objeto_crear'),
    
]
