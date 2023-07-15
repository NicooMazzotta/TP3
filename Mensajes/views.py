from django.shortcuts import render, redirect, get_object_or_404
from Mensajes.models import Chat, Mensaje
from Mensajes.forms import EnviarMensaje
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def vista_mensajes(request):
    
    usuario = request.user
    
    cantidad_chats_sin_leer = Chat.objects.filter(usuario_1=usuario,leido=False).count()
    chats = Chat.objects.filter(usuario_1=usuario).order_by('-fecha_ultima_actualizacion')
    
    informacion_chats = {'cantidad_chats_sin_leer': cantidad_chats_sin_leer,
                         'chats': chats}
    
    return render(request, 'Mensajes/vista_mensajes.html',informacion_chats)


@login_required
def listar_usuarios(request):
    usuarios = User.objects.exclude(id=request.user.id)
    return render(request, 'Mensajes/listar_usuarios.html', {'usuarios': usuarios})

@login_required
def chat(request, usuario_id):
    
    usuario_actual = request.user
    usuario_destino = get_object_or_404(User, id=usuario_id)
    
    chat = Chat.objects.filter(usuario_1=usuario_actual, usuario_2=usuario_destino).first()
    
    if chat is None:
        chat = Chat(usuario_1=usuario_actual, usuario_2=usuario_destino)
    chat.leido = True
    chat.save()
    
    chat_2 = Chat.objects.filter(usuario_1=usuario_destino, usuario_2=usuario_actual).first()
    
    if chat_2 is None:
        chat_2 = Chat(usuario_1=usuario_destino, usuario_2=usuario_actual)
        chat_2.save()
    
    
    mensajes = Mensaje.objects.filter(conversacion=chat)
        
    formulario = EnviarMensaje()
    if request.method == 'POST':
        formulario = EnviarMensaje(request.POST)
        if formulario.is_valid():
            contenido = formulario.cleaned_data['contenido']
            mensaje = Mensaje(conversacion=chat, remitente=usuario_actual, contenido=contenido)
            mensaje.save()
            
            mensaje_2 = Mensaje(conversacion=chat_2, remitente=usuario_actual, contenido=contenido)
            mensaje_2.save()
            chat_2.leido = False
            chat_2.save()
            
            return redirect('Mensajes:chat', usuario_id=usuario_id)
    
    informacion = {'chat': chat,
                   'mensajes': mensajes,
                   'formulario': formulario}
    
    return render(request, 'Mensajes/chat.html', informacion)