from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from inicio.models import Objeto
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from inicio.forms import BuscarObjeto
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request, 'inicio/inicio.html')

class CrearObjeto(LoginRequiredMixin, CreateView):
    model = Objeto
    template_name = 'inicio/objeto_crear.html'
    fields = ['imagen','Nombre','tipo','precio','descripcion']
    success_url = reverse_lazy('inicio:objetos_vendedor')
    
    def form_valid(self, form):
        form.instance.vendedor = self.request.user
        return super().form_valid(form)

class ListarObjetos(ListView):
    model = Objeto
    template_name = "inicio/objetos_vendedor.html"
    context_object_name = 'objetos'
    
    def get_queryset(self):
        
        listado_de_objetos=[]
        
        formulario = BuscarObjeto(self.request.GET)
        if formulario.is_valid():
            nombre_a_buscar = formulario.cleaned_data['Nombre']
            listado_de_objetos = Objeto.objects.filter(Nombre__icontains=nombre_a_buscar,en_venta = True,  vendedor=self.request.user)
        else:
            listado_de_objetos = Objeto.objects.filter(en_venta = True,vendedor=self.request.user)
            
        return listado_de_objetos
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['formulario'] = BuscarObjeto()
        
        return contexto
    
class ModificarObjeto(LoginRequiredMixin, UpdateView):
    model = Objeto
    template_name = "inicio/objeto_modificar.html"
    fields = ['imagen','Nombre','tipo','precio','descripcion']
    success_url = reverse_lazy('inicio:objetos_vendedor')  
    
class EliminarObjeto(LoginRequiredMixin, DeleteView):
    model = Objeto
    template_name = "inicio/objeto_eliminar.html"
    success_url = reverse_lazy('inicio:objetos_vendedor')
    
class MostrarObjetos(LoginRequiredMixin, DetailView):
    model = Objeto
    template_name = "inicio/objeto_mostrar.html"
    
def objetos(request):
    return render(request, 'inicio/objetos.html')

class ListarObjetosVendidos(LoginRequiredMixin, ListView):
    model = Objeto
    template_name = "inicio/objetos_historial_vendidos.html"
    context_object_name = 'objetos'
    
    def get_queryset(self):
        
        listado_de_objetos=[]
        formulario = BuscarObjeto(self.request.GET)
        if formulario.is_valid():
            nombre_a_buscar = formulario.cleaned_data['Nombre']
            listado_de_objetos = Objeto.objects.filter(Nombre__icontains = nombre_a_buscar, en_venta = False)
        else:
            queryset = Objeto.objects.filter(en_venta=False)
            return queryset

        
        return listado_de_objetos
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['formulario'] = BuscarObjeto()
        
        return contexto
    
        
class ListarObjetosDisponibles(ListView):
    model = Objeto
    template_name = "inicio/objetos_comprador.html"
    context_object_name = 'objetos'
    
    def get_queryset(self):
        
        listado_de_objetos=[]
        
        formulario = BuscarObjeto(self.request.GET)
        if formulario.is_valid():
            nombre_a_buscar = formulario.cleaned_data['Nombre']
            listado_de_objetos = Objeto.objects.filter(Nombre__icontains=nombre_a_buscar, en_venta=True).exclude(vendedor=self.request.user)
        else:
            queryset = Objeto.objects.filter(en_venta=True).exclude(vendedor=self.request.user)
            return queryset

        
        return listado_de_objetos
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['formulario'] = BuscarObjeto()
        
        return contexto
    
def confirmar_compra(request, objeto_id):
    mensaje = {}
    objeto = get_object_or_404(Objeto, id=objeto_id)
    
    if objeto.vendedor == request.user:
        mensaje =  'No puedes comprar un objeto que tú mismo publicaste.'
        return render(request, 'inicio/objeto_confirmar_compra.html', {'mensaje': mensaje})
    
    if request.method == 'POST':
        objeto.en_venta = False
        objeto.comprador = request.user
        objeto.save()
        return redirect('inicio:objetos_historial_comprados')
    
    return render(request, 'inicio/objeto_confirmar_compra.html', {'objeto': objeto})

class ListarObjetosComprados(LoginRequiredMixin, ListView):
    model = Objeto
    template_name = "inicio/objetos_historial_comprados.html"
    context_object_name = 'objetos'
    
    def get_queryset(self):
        
        listado_de_objetos=[]
        formulario = BuscarObjeto(self.request.GET)
        if formulario.is_valid():
            nombre_a_buscar = formulario.cleaned_data['Nombre']
            listado_de_objetos = Objeto.objects.filter(Nombre__icontains = nombre_a_buscar, en_venta = False, comprador= self.request.user)
        else:
            queryset = Objeto.objects.filter(en_venta = False, comprador= self.request.user)
            return queryset


        return listado_de_objetos
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['formulario'] = BuscarObjeto()
        
        return contexto
    
