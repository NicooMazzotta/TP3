from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class CreacionUsuarios(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='repetir contrasenia', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']
        help_texts = {k:"" for k in fields}
    
class EdicionUsuarios(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(required=False,label='Nombre', max_length=20)    
    last_name = forms.CharField(required=False,label='Apellido', max_length=20)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name','last_name', 'avatar',]