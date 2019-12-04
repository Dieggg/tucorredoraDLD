from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.propiedad.views import index
from apps.propiedad.views import TipoInmuebleList, TipoInmuebleCreate, TipoInmuebleUpdate, TipoInmuebleDelete
from apps.propiedad.views import InmuebleList, InmuebleCreate, InmuebleUpdate, InmuebleDelete

urlpatterns = [
    path('', index, name='index'),

    path('nuevo', login_required(TipoInmuebleCreate.as_view()), name="tipo_inmueble_nuevo"), 
    path('listar', login_required(TipoInmuebleList.as_view()), name="tipo_inmueble_listar"),
    path('actualizar/<int:pk>', login_required(TipoInmuebleUpdate.as_view()), name="tipo_inmueble_actualizar"),  
    path('eliminar/<int:pk>', login_required(TipoInmuebleDelete.as_view()), name="tipo_inmueble_eliminar"),

    path('nuevo_inmueble', login_required(InmuebleCreate.as_view()), name="inmueble_nuevo"),  
    path('listar_inmueble', login_required(InmuebleList.as_view()), name="inmueble_listar"),
    path('actualizar_inmueble/<int:pk>', login_required(InmuebleUpdate.as_view()), name="inmueble_actualizar"),  
    path('eliminar_inmueble/<int:pk>', login_required(InmuebleDelete.as_view()), name="inmueble_eliminar"),   
]