from django import forms

class EnviarMensaje(forms.Form):
    contenido = forms.CharField(widget=forms.Textarea)