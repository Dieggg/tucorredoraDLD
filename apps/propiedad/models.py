from django.db import models
from apps.persona.models import Persona
from cloudinary.models import CloudinaryField

# Create your models here.
class TipoInmueble(models.Model):
    descripcion = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.descripcion)

class Region(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.nombre)

class Provincia(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)

class Comuna(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)
    

class Inmueble(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    tipo_inmueble = models.ForeignKey(TipoInmueble, on_delete=models.CASCADE)
    calle = models.CharField(max_length=150, null=True, blank=False )
    numero = models.CharField(max_length=7, null=True, blank=False)
    detalle = models.CharField(max_length=255, null=True, blank=True)
    codigo_postal = models.IntegerField(null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default='')
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, default='')
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, default='')



