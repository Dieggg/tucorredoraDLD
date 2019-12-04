from django.urls import path
from apps.usuario.views import RegistroUsuario, DeleteUsuario
from apps.usuario import views


urlpatterns = [
    path('', views.index, name='index_usuario'),
    path('registrar', RegistroUsuario.as_view(), name="usuario_registrar"),  
    path('eliminar/<int:pk>', DeleteUsuario.as_view(), name="usuario_eliminar"),  
]