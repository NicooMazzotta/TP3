from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
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
    success_url = reverse_lazy('inicio:objetos')
    
    def form_valid(self, form):
        form.instance.vendedor = self.request.user
        return super().form_valid(form)
    
class Objetos(LoginRequiredMixin, ListView):
    model = Objeto
    template_name = "inicio/objetos.html"
    context_object_name = 'objetos'
    
class ListarObjetos(ListView):
    model = Objeto
    template_name = "inicio:objetos.html"
    context_object_name = 'objetos'
    
    def get_queryset(self):
        
        listado_de_objetos=[]
        
        formulario = BuscarObjeto(self.request.GET)
        if formulario.is_valid():
            nombre_a_buscar = formulario.cleaned_data['Nombre']
            listado_de_objetos = Objeto.objects.filter(nombre__icontains=nombre_a_buscar)
        
        return listado_de_objetos
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['formulario'] = BuscarObjeto()
        
        return contexto
    
class ModificarObjeto(LoginRequiredMixin, UpdateView):
    model = Objeto
    template_name = "inicio/objeto_modificar.html"
    fields = ['imagen','Nombre','tipo','precio','descripcion']
    success_url = reverse_lazy('inicio:objetos')  
    
class EliminarObjeto(LoginRequiredMixin, DeleteView):
    model = Objeto
    template_name = "inicio/objeto_eliminar.html"
    success_url = reverse_lazy('inicio:objetos')
    
class MostrarObjetos(LoginRequiredMixin, DetailView):
    model = Objeto
    template_name = "inicio/objeto_mostrar.html"