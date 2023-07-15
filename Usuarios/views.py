from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Usuarios.forms import CreacionUsuarios, EdicionUsuarios
from django.urls import reverse_lazy
from Usuarios.models import InfoExtra

def usuario(request):
    return render(request, 'Usuarios/usuario.html')

def usuario_registrar(request):
    
    if request.method == "POST":
        formulario = CreacionUsuarios(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Usuarios:usuario_acceder')
            
        else:
            return render(request, 'Usuarios/usuario_registrar.html', {'formulario': formulario})
    
    formulario = CreacionUsuarios()
    return render(request, 'Usuarios/usuario_registrar.html', {'formulario': formulario})
    
def usuario_acceder(request):
    if request.method == "POST":
        formulario= AuthenticationForm(request, data =request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contrasenia = formulario.cleaned_data['password']
            
            user = authenticate(username = usuario, password = contrasenia)
            
            login(request, user)
            
            InfoExtra.objects.get_or_create(user=user)
            
            return redirect('inicio:inicio')
        else:
            return render(request, 'Usuarios/usuario_acceder.html', {'formulario': formulario})
    
    
    formulario= AuthenticationForm()
    return render(request, 'Usuarios/usuario_acceder.html', {'formulario': formulario})

def usuario_perfil(request):
    return render(request, 'Usuarios/usuario_perfil.html')


@login_required
def usuario_editar_perfil(request):

    info_extra_user = request.user.infoextra
    
    if request.method == "POST":
        formulario = EdicionUsuarios(request.POST,request.FILES , instance= request.user)
        if formulario.is_valid():
            avatar = formulario.cleaned_data.get('avatar')
            if avatar:
                info_extra_user.avatar = avatar
                info_extra_user.save()
            
            formulario.save()
            return redirect('Usuarios:usuario_perfil')
            
    else:
        formulario = EdicionUsuarios(initial={'avatar': info_extra_user.avatar},instance= request.user)
            
    return render(request, 'Usuarios/usuario_editar_perfil.html', {'formulario': formulario})



class CustomPasswordChangeForm(PasswordChangeForm):
    error_messages = {
        'password_incorrect': 'La contraseña actual es incorrecta.',
        'password_mismatch': 'Las contraseñas nuevas no coinciden.',
        'password_weak': 'La contraseña es demasiado débil.',
    }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].label = 'Contraseña actual'
        self.fields['new_password1'].label = 'Contraseña nueva'
        self.fields['new_password2'].label = 'Confirmar contraseña nueva'
        
    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')
        
        return password1

class EditarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'Usuarios/usuario_editar_contrasenia.html'
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('Usuarios:usuario_perfil')