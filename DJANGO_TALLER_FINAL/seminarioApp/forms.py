from dataclasses import fields
from datetime import datetime
from email.policy import default
from django import forms
from django.forms import TextInput, ValidationError
from django.core.validators import RegexValidator
from seminarioApp.models import Inscritos, Institucion

estados = [
    ('RESERVADO','RESERVADO'),
    ('COMPLETADA','COMPLETADA'),
    ('ANULADA', 'ANULADA'),
    ('NO ASISTEN','NO ASISTEN'),
]


class FormInscritos(forms.ModelForm):
    nombre = forms.CharField(required=True, error_messages={'invalid':'Formato invalido'}, widget=forms.TextInput(attrs={'class': 'form-control', 'pattern':'[A-Za-z ]+'}))
    telefono = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    fecha_inscripcion = forms.DateTimeField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'date'}))
    institucion = forms.ModelChoiceField(required=True, queryset=Institucion.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    hora_inscripcion = forms.TimeField(required=True, error_messages={'invalid':"Ingrese una hora valida"}, widget=forms.TimeInput(attrs={'class': 'form-control'}))
    estado = forms.ChoiceField(required=True,choices=estados, widget=forms.Select(attrs={'class':'form-control'}))
    observacion = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Inscritos
        fields = [
                'nombre', 
                'telefono', 
                'fecha_inscripcion', 
                'institucion', 
                'hora_inscripcion', 
                'estado', 
                'observacion'
                ]
    
    #Validaciones
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre)>50:
            raise forms.ValidationError("Maximo 50 caracteres")
        return nombre

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if len(telefono)>25:
            raise forms.ValidationError("Maximo 25 caracteres")
        return telefono

    def clean_estados(self):
        estado = self.cleaned_data.get('estado')
        if estados in estado:
            return estado
        else:
            raise forms.ValidationError("Error en select")

    def clean_observacion(self):
        observacion = self.cleaned_data.get('observacion')
        if len(observacion)>200:
            raise forms.ValidationError("Maximo 200 caracteres")
        return observacion



