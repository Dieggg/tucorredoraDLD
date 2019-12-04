from django import forms
from django.forms import ModelForm

from .models import TipoInmueble, Inmueble 

class TipoInmuebleForm(ModelForm):
    class Meta:
        model = TipoInmueble
        fields = [
            'descripcion',             
        ]

        labels = {
            'descripcion': 'Tipo de inmueble (Ej. Casa, Dpto, Dpto-Casa, Penthouse)',
            'dv':'Digito verificador',
            'movil':'Teléfono movil',
            'fijo':'Telefono fijo',
            'esCliente': 'Es cliente' 
        }
        widgets = {
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            
        }

class InmuebleForm(ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            'propietario',
            'tipo_inmueble',
            'calle',
            'numero',
            'detalle',
            'codigo_postal',
            'region',
            'provincia',
            'comuna',
        ]

        labels = {
            'propietario': 'Propietario',
            'tipo_inmueble':'Tipo de inmueble',
            'calle': 'Calle',
            'numero': 'Numero',
            'detalle': 'Detalle (dpto, block, etc)',
            'codigo_postal':'Codigo postal',
            'region':'Región',
            'provincia':'Provincia',
            'comuna':'Comuna',
        }

        widgets = {
            'propietario': forms.Select(attrs={'class':'form-control'}),
            'tipo_inmueble': forms.Select(attrs={'class':'form-control'}),
            'calle':forms.TextInput(attrs={'class':'form-control'}),
            'numero':forms.TextInput(attrs={'class':'form-control'}),
            'detalle':forms.TextInput(attrs={'class':'form-control'}),
            'codigo_postal':forms.TextInput(attrs={'class':'form-control'}),
            'region':forms.Select(attrs={'class':'form-control'}),
            'provincia':forms.Select(attrs={'class':'form-control'}),
            'comuna':forms.Select(attrs={'class':'form-control'}),
        }



        


