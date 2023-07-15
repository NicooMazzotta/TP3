from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    usuario_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversaciones_1')
    usuario_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversaciones_2')
    leido = models.BooleanField(default=False)
    fecha_ultima_actualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat con {self.usuario_2}"
    
    class Meta:
        ordering = ['-fecha_ultima_actualizacion']

class Mensaje(models.Model):
    conversacion = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='mensajes')
    remitente = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.remitente}"
    
    def mostrar_fecha_hora(self):
        return self.fecha_envio.strftime("enviado el %d/%m/%Y a las %H:%M")
