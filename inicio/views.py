from django.shortcuts import render, redirect
from inicio.forms import CrearVendedor, CrearComprador, CrearObjeto, AccederUsuario, BuscarObjeto
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
            email = informacion['Email']
            
            if Comprador.objects.filter(Email=email).exists():
                mensaje = 'El correo electronico ya fue registrado. Por favor, intente con otro'
            else:
                comprador = Comprador(Email=informacion['Email'],Nombre_usuario=informacion['Nombre_usuario'],contrasenia=informacion['contrasenia'],Direccion_entregas=informacion['Direccion_entregas'])
                comprador.save()
                mensaje = f'Se creo el comprador: {comprador.Nombre_usuario} - Existosamente!'
                return render(request, 'inicio/comprador_creado.html', {'comprador' : comprador, 'mensaje': mensaje})
        else:
            return render(request, 'inicio/comprador_crear.html', {'formulario' : formulario})
    
    formulario = CrearComprador()
    return render(request, 'inicio/comprador_crear.html', {'formulario' : formulario, 'mensaje': mensaje})

def comprador_acceder(request):
    mensaje = ''
    formulario = AccederUsuario(request.GET)
    if formulario.is_valid():
        informacion = formulario.cleaned_data
        email_a_buscar = informacion['Email']
        contrasenia_a_buscar = informacion['contrasenia']
        
        try:
            comprador = Comprador.objects.get(Email=email_a_buscar, contrasenia= contrasenia_a_buscar)
            return render(request, 'inicio/comprador_creado.html', {'comprador': comprador})
        except Comprador.DoesNotExist:
            mensaje = 'No se pudo iniciar'
        
    formulario = AccederUsuario()
    return render(request, 'inicio/comprador_acceder.html', {'formulario': formulario, 'mensaje': mensaje})

def vendedor(request):
    return render(request, 'inicio/vendedor.html')

def vendedor_crear(request):
    
    mensaje = ''
    
    if(request.method == "POST"):
        formulario = CrearVendedor(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            email = informacion['Email']
            
            if Vendedor.objects.filter(Email=email).exists():  
                mensaje = 'el correo electronico ya fue. Por favor, intente con otro'
            else:
                vendedor = Vendedor(Email=informacion['Email'],Nombre_usuario=informacion['Nombre_usuario'],contrasenia=informacion['contrasenia'], Direccion_tienda=informacion['Direccion_tienda'])
                vendedor.save()
                mensaje = f'Se creo el vendedor: {vendedor.Nombre_usuario} - Existosamente!'
                return render(request, 'inicio/vendedor_creado.html', {'vendedor' : vendedor, 'mensaje': mensaje})
        else:
            return render(request, 'inicio/vendedor_crear.html', {'formulario' : formulario})
    
    formulario = CrearVendedor()
    return render(request, 'inicio/vendedor_crear.html', {'formulario' : formulario, 'mensaje': mensaje})


def vendedor_acceder(request):
    mensaje = ''
    formulario = AccederUsuario(request.GET)
    if formulario.is_valid():
        informacion = formulario.cleaned_data
        email_a_buscar = informacion['Email']
        contrasenia_a_buscar = informacion['contrasenia']
        
        try:
            vendedor = Vendedor.objects.get(Email=email_a_buscar, contrasenia= contrasenia_a_buscar)
            return render(request, 'inicio/vendedor_creado.html', {'vendedor': vendedor})
        except Vendedor.DoesNotExist:
            print("llegue aca")
            mensaje = 'No se pudo iniciar'
        
    formulario = AccederUsuario()
    return render(request, 'inicio/vendedor_acceder.html', {'formulario': formulario, 'mensaje': mensaje})

def objetos(request):
    formulario = BuscarObjeto(request.GET)
    if formulario.is_valid():
        nombre_objeto = formulario.cleaned_data['Nombre']
        listado_objetos = Objeto.objects.filter(Nombre__icontains=nombre_objeto)
        
    formulario = BuscarObjeto()    
    return render(request, 'inicio/objetos.html', {'formulario': formulario, 'objetos': listado_objetos})

def objeto_crear(request):
    
    mensaje = ''
    
    if(request.method == "POST"):
        formulario = CrearObjeto(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            objeto = Objeto(Nombre=informacion['Nombre'],tipo=informacion['tipo'],descripcion=informacion['descripcion'])
            objeto.save()
            mensaje = f'Se creo el objeto: {objeto.Nombre} - Existosamente!'
            return redirect('inicio:objetos')
        else:
            return render(request, 'inicio/objeto_crear.html', {'formulario' : formulario})
    
    
    formulario = CrearObjeto()
    return render(request, 'inicio/objeto_crear.html', {'formulario' : formulario, 'mensaje': mensaje})