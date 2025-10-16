from django import forms
from .models import Estado, Municipio

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['nombre']
        labels = {'nombre': 'Nombre del Estado'}
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'input-text',
                'placeholder': 'Ej. Guanajuato'
            })
        }

class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = ['nombre', 'estado']
        labels = {
            'nombre': 'Nombre del Municipio',
            'estado': 'Estado al que pertenece'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'input-text',
                'placeholder': 'Ej. Salamanca'
            }),
            'estado': forms.Select(attrs={'class': 'input-select'})
        }
