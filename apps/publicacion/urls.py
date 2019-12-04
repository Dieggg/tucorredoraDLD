from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nuevo', views.propietario_view, name='propietario_view'),
    
]