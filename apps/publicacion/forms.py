from django import forms
from apps.publicacion.models import Propietario

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = [
            'nombre',
            'apellidos',
            'rut',
            'dv',
            'movil',
            'fijo',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellidos':'Apellidos',
            'rut':'Rut',
            'dv':'Digito verificador',
            'movil':'Teléfono movil',
            'fijo':'Telefono fijo',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos':forms.TextInput(attrs={'class':'form-control'}),
            'rut':forms.TextInput(attrs={'class':'form-control'}),
            'dv':forms.TextInput(attrs={'class':'form-control'}),
            'movil':forms.TextInput(attrs={'class':'form-control'}),
            'fijo':forms.TextInput(attrs={'class':'form-control'}),
        }



