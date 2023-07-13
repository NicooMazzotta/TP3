from django.urls import path, include
from Usuarios import views
from django.contrib.auth.views import LogoutView

app_name = "Usuarios"

urlpatterns = [
    path('', views.usuario, name='usuario'),
    path('registrar/', views.usuario_registrar, name='usuario_registrar'),
    path('acceder/', views.usuario_acceder, name='usuario_acceder'),
    path('desconectar/', LogoutView.as_view(template_name='Usuarios/usuario_desconectar.html'), name='usuario_desconectar'),
    path('perfil/', views.usuario_perfil, name='usuario_perfil'),
    path('perfil/editar', views.usuario_editar_perfil, name='usuario_editar_perfil'),
    path('perfil/editar/contrasenia', views.EditarContrasenia.as_view(), name='usuario_editar_contrasenia'),
]
