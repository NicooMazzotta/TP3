from django.shortcuts import render
from inicio.forms import CrearVendedor, CrearComprador, CrearObjeto, AccederComprador, AccederVendedor
from inicio.models import Vendedor, Comprador, Objeto

def inicio(request):
    return render(request, 'inicio/inicio.html')

def comprador(request):
    return render(request, 'inicio/comprador.html')

def comprador_crear(request):
    
    mensaje = ''
    
    if(request.method == "POST"):
        formulario = CrearComprador(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            comprador = Comprador(Email=informacion['Email'],Nombre_usuario=informacion['Nombre_usuario'],contrasenia=informacion['contrasenia'],Direccion_entregas=informacion['Direccion_entregas'])
            comprador.save()
            mensaje = f'Se creo el usuario: {comprador.Nombre_usuario} - Existosamente!'
        else:
            return render(request, 'inicio/comprador_crear.html', {'formulario' : formulario})
    
    formulario = CrearComprador()
    return render(request, 'inicio/comprador_crear.html', {'formulario' : formulario, 'mensaje': mensaje})

def comprador_acceder(request):
    formulario = AccederComprador()
    return render(request, 'inicio/comprador_acceder.html', {'formulario' : formulario})

def vendedor(request):
    return render(request, 'inicio/vendedor.html')

def vendedor_crear(request):
    formulario = CrearVendedor()
    return render(request, 'inicio/vendedor_crear.html', {'formulario' : formulario})

def vendedor_acceder(request):
    formulario = AccederVendedor()
    return render(request, 'inicio/vendedor_acceder.html', {'formulario' : formulario})