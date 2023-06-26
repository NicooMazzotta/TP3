from django.db import models

# Create your models here.
# class cliente(models.Model):
    
#     def __init__(self, nombre, direccion, correo, objetos_comprados):
#         self.nombre = nombre
#         self.direccion = direccion
#         self.correo = correo
#         self.objetos_comprados = objetos_comprados
        
#     def __str__(self):
#         return f'Cliente: {self.nombre}, correo: {self.correo}, Direccion de entregas: {self.direccion}'

#     def comprar(self, objeto, marca):
#         self.objetos_comprados.append((objeto, marca))
#         print(f"se compro exitosamente {objeto} de la marca {marca}")

#     def listar_compras(self):
#         for compra in self.objetos_comprados:
#             objeto, marca = compra
#             print(f"Compro {objeto} de {marca}")
