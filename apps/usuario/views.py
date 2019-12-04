from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'index_usuario.html')

class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuario_registrar.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('usuario:index.html')

class DeleteUsuario(DeleteView):
    model = User
    template_name = 'usuario_delete.html'
    success_url = reverse_lazy('persona:persona_listar')