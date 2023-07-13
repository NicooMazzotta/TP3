from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Objeto(models.Model):
    Nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    descripcion = RichTextField(null=True)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='imagen')
    fecha_publicacion = models.DateField(auto_now_add=True)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    en_venta = models.BooleanField(default=True)
    comprador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='compras')

    def __str__(self):
        return f'{self.Nombre}, de  valor ${self.precio} - publicado el {self.fecha_publicacion.strftime("%d/%m/%Y")}'