from django.db import models

# Create your models here.
class Usuario(models.Model): 
    Email = models.CharField(max_length=30)
    Nombre_usuario = models.CharField(max_length=20)
    contrasenia = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.Nombre_usuario} - {self.Email}'
    
class Objeto(models.Model):
    Nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.Nombre} - {self.tipo} - {self.descripcion}'
    
class Comprador(Usuario):
    Direccion_entregas = models.CharField(max_length=20)
    Objetos_comprados = models.ManyToManyField(Objeto)
    
    def listar_objetos_comprados(self):
        return self.Objetos_comprados.all()
    
class Vendedor(Usuario):
    Direccion_tienda = models.CharField(max_length=20)
    Objetos_vendidos = models.ManyToManyField(Objeto)
    
    def listar_objetos_vendidos(self):
        return self.Objetos_vendidos.all()

    