from django import forms
from ckeditor.fields import RichTextFormField

class ObjetoBase(forms.Form):
    Nombre = forms.CharField(max_length=20)
    tipo = forms.CharField(max_length=20)
    precio = forms.IntegerField()
    imagen = forms.ImageField()
    descripcion =RichTextFormField(required=False)
    
class BuscarObjeto(forms.Form):
    Nombre = forms.CharField(max_length=20, required=False)
    
class CrearObjeto(ObjetoBase):
    ...

class ModificarObjeto(ObjetoBase):
    ...