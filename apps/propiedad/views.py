from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.propiedad.models import TipoInmueble, Inmueble
from apps.propiedad.forms import TipoInmuebleForm, InmuebleForm
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'index.html')

class TipoInmuebleList(ListView):
    model = TipoInmueble
    template_name = 'tipo_inmueble_listar.html'

class TipoInmuebleCreate(CreateView):
    model = TipoInmueble
    form_class = TipoInmuebleForm
    template_name = 'tipo_inmueble_form.html'
    success_url = reverse_lazy('propiedad:tipo_inmueble_listar')

class TipoInmuebleUpdate(UpdateView):
    model = TipoInmueble
    form_class = TipoInmuebleForm
    template_name = 'tipo_inmueble_form.html'
    success_url = reverse_lazy('propiedad:tipo_inmueble_listar')

class TipoInmuebleDelete(DeleteView):
    model = TipoInmueble
    template_name = 'tipo_inmueble_delete.html'
    success_url = reverse_lazy('propiedad:tipo_inmueble_listar')

class InmuebleList(ListView):
    model = Inmueble
    template_name = 'inmueble_listar.html'

class InmuebleCreate(CreateView):
    model = Inmueble
    form_class = InmuebleForm
    template_name = 'inmueble_form.html'
    success_url = reverse_lazy('propiedad:inmueble_listar')

class InmuebleUpdate(UpdateView):
    model = Inmueble
    form_class = InmuebleForm
    template_name = 'inmueble_form.html'
    success_url = reverse_lazy('propiedad:inmueble_listar')

class InmuebleDelete(DeleteView):
    model = Inmueble
    template_name = 'inmueble_delete.html'
    success_url = reverse_lazy('propiedad:inmueble_listar')
    
