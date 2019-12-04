from django.db import models
from django.utils import timezone

# Create your models here.
# Create your models here.
# - Inmuebles > Tipo
# - Caracteristica
# - Direccion 
# - Region > Prinvicia > Comuna > Sector
# - Imagenes
# - Propietario
# - Anuncio
# - BitacoraContactos
# - Requisitos 
# - Cliente (flag esCliente = bool)

class Region(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)

class Provincia(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class Comuna(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

class Sector(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class TipoInmueble(models.Model):
    descripcion = models.CharField(max_length=50, null=False, blank=False)

class Propietario(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellidos = models.CharField(max_length=50, null=False, blank=False)
    rut = models.IntegerField(null=False, blank=False, unique=True)
    dv = models.CharField(max_length=1, null=False, blank=False)
    movil = models.IntegerField(null=False, blank=False)
    fijo = models.IntegerField(null=True, blank=True)

class Inmueble(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    tipo_inmueble = models.ForeignKey(TipoInmueble, on_delete=models.CASCADE)

class Direccion(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    calle = models.CharField(max_length=150, null=False, blank=False)
    numero = models.CharField(max_length=7, null=False, blank=False)
    detalle = models.CharField(max_length=255, null=True, blank=True)
    codigo_postal = models.IntegerField(null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)

class TipoContenido(models.Model):
    descripcion = models.CharField(max_length=25, null=False, blank=False)

class Galeria(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    tipo_contenido = models.ForeignKey(TipoContenido, on_delete=models.CASCADE)
    #contenido = CloudinaryField('image')

class Anuncio(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    creacion = models.DateTimeField(default=timezone.now)
    modificacion = models.DateTimeField(default=timezone.now)
    publicacion = models.DateTimeField(null=True, blank=True)

class Requisito(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50, null=False, blank=False)
    cantidad = models.IntegerField()
    obligatorio = models.BooleanField(default=True)

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    movil = models.IntegerField()
    fijo = models.IntegerField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre


class BitacoraContactos(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    consulta = models.DateTimeField(default=timezone.now)


    class Meta:
        verbose_name = "BitacoraContacto"
        verbose_name_plural = "BitacoraCotactos"

    def __str__(self):
        return self.cliente
