from django.contrib import admin
from .models import TipoInmueble, Inmueble, Region,Provincia,Comuna

# Register your models here.
admin.site.register(TipoInmueble)
admin.site.register(Inmueble)
admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)