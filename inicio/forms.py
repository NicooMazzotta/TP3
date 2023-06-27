from django import forms

class CrearVendedor(forms.Form):
    Email = forms.CharField(max_length=30)
    Nombre_usuario = forms.CharField(max_length=20)
    contrasenia = forms.CharField(max_length=20)
    Direccion_tienda = forms.CharField(max_length=20, required=False)
    
class AccederVendedor(forms.Form):
    Email = forms.CharField(max_length=30)
    contrasenia = forms.CharField(max_length=20)
    
class CrearComprador(forms.Form):
    Email = forms.CharField(max_length=30)
    Nombre_usuario = forms.CharField(max_length=20)
    contrasenia = forms.CharField(max_length=20)
    Direccion_entregas = forms.CharField(max_length=20)
    
class AccederComprador(forms.Form):
    Email = forms.CharField(max_length=30)
    contrasenia = forms.CharField(max_length=20)
    
class CrearComprador(forms.Form):
    Email = forms.CharField(max_length=30)
    Nombre_usuario = forms.CharField(max_length=20)
    contrasenia = forms.CharField(max_length=20)
    Direccion_entregas = forms.CharField(max_length=20)
    
class CrearObjeto(forms.Form):
    Nombre = forms.CharField(max_length=20)
    tipo = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=500)