from django.shortcuts import render
from django.http import HttpResponse

from apps.publicacion.forms import PersonaForm
from apps.publicacion.models import Propietario
from django.views.generic import ListView


# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def propietario_view(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('publicacion:index')
    else:
        form = PersonaForm()
    
    return render(request, 'propietario_form.html', {'form': form })

class PropietarioList(ListView):
    model = Propietario
    template_name = 'propietario_list.html'