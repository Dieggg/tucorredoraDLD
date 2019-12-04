from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.persona.views import index, RegistroPersona, ListarPersona, UpdatePersona, DeletePersona


urlpatterns = [
    path('', index, name='index_persona'),
    path('nuevo', login_required(RegistroPersona.as_view()), name="persona_nuevo"),
    path('listar', login_required(ListarPersona.as_view()), name="persona_listar"), 
    path('actualizar/<int:pk>', login_required(UpdatePersona.as_view()), name="persona_actualizar"),  
    path('eliminar/<int:pk>', login_required(DeletePersona.as_view()), name="persona_eliminar"),  
]