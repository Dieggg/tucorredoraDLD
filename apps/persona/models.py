from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Persona(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    rut = models.CharField(max_length=10,null=False, blank=False, unique=True)
    dv = models.CharField(max_length=1, null=False, blank=False)  
    movil = models.IntegerField(null=False, blank=False)
    fijo = models.IntegerField(null=True, blank=True)
    esCliente = models.NullBooleanField(default=None)
    imagen = CloudinaryField('image', null=True)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


