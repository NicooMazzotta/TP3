from django import forms

class CrearUsuario(forms.Form):
    Email = forms.EmailField(max_length=30)
    Nombre_usuario = forms.CharField(max_length=20)
    contrasenia = forms.CharField(max_length=20)
    
class AccederUsuario(forms.Form):
    Email = forms.EmailField(max_length=30)
    contrasenia = forms.CharField(max_length=20)

class CrearVendedor(CrearUsuario):
    Direccion_tienda = forms.CharField(max_length=20, required=False)
    
class CrearComprador(CrearUsuario):
    Direccion_entregas = forms.CharField(max_length=20)
    
class CrearObjeto(forms.Form):
    Nombre = forms.CharField(max_length=20)
    tipo = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=50)
    
class BuscarObjeto(forms.Form):
    Nombre = forms.CharField(max_length=20, required=False)