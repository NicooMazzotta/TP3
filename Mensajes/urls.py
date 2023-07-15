from django.urls import path
from Mensajes import views

app_name = "Mensajes"

urlpatterns = [
   path('mensajes/', views.vista_mensajes, name='mensajes'),
   path('mensajes/listar_usuarios', views.listar_usuarios, name='listar_usuarios'),
   path('mensajes/chat/<int:usuario_id>/', views.chat, name='chat')
   
]
