from django.contrib import admin
from inicio.models import Usuario, Vendedor, Comprador, Objeto

# Register your models here.

admin.site.register(Objeto)
admin.site.register(Comprador)
admin.site.register(Vendedor)