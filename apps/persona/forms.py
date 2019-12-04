from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Persona

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = [
            'rut',
            'dv',
            'movil',
            'fijo',
            'esCliente',
        ]

        labels = {
            'rut': 'RUT',
            'dv':'Digito verificador',
            'movil':'Teléfono movil',
            'fijo':'Telefono fijo',
            'esCliente': 'Es cliente',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class':'form-control'}),
            'dv': forms.TextInput(attrs={'class':'form-control'}),
            'movil':forms.TextInput(attrs={'class':'form-control'}),
            'fijo':forms.TextInput(attrs={'class':'form-control'}), 
            'esCliente': forms.CheckboxInput(attrs={'class': 'required checkbox form-control'}),   
        }


