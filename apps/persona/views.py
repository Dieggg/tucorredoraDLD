from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from .forms import PersonaForm
from apps.usuario.forms import RegistroUser
from apps.persona.models import Persona


from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'index_usuario.html')

class ListarPersona(ListView):
    model = Persona
    template_name = 'persona_list.html'

class RegistroPersona(CreateView):
    model = User
    template_name = 'persona_registrar.html'
    form_class = PersonaForm
    second_form_class = RegistroUser
    success_url = reverse_lazy('persona:persona_listar')

    def get_context_data(self, **kwargs):
        context = super(RegistroPersona, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            persona = form.save(commit=False)
            persona.user = form2.save()
            
            persona.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class UpdatePersona(UpdateView):
    model = Persona
    template_name = 'persona_registrar.html'
    form_class = PersonaForm
    second_form_class = RegistroUser
    success_url = reverse_lazy('persona:persona_listar')

    def get_context_data(self, **kwargs):
        context = super(UpdatePersona, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        persona = self.model.objects.get(id=pk)
        user = persona.user
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=user)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_persona = kwargs['pk']
        persona = self.model.objects.get(id=id_persona)
        user = persona.user
        
        form = self.form_class(request.POST, instance=persona)
        form2 = self.second_form_class(request.POST, instance=user)
        if form.is_valid() and form2.is_valid():
            persona = form.save(commit=False)
            persona.user = form2.save()
            
            persona.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class DeletePersona(DeleteView):
    model = User
    template_name = 'persona_delete.html'
    success_url = reverse_lazy('persona:persona_listar')
    

    



