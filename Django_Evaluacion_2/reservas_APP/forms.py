from dataclasses import fields
from datetime import datetime
from email.policy import default
from django import forms
from django.forms import TextInput, ValidationError
from django.core.validators import RegexValidator
from reservas_APP.models import reservas

estados = [
    ('RESERVADO','RESERVADO'),
    ('COMPLETADA','COMPLETADA'),
    ('ANULADA', 'ANULADA'),
    ('NO ASISTEN','NO ASISTEN'),
]

#algunos mensajes de error no se muestran con el estilo correcto

class FormReservas(forms.ModelForm):
    nombre = forms.CharField(required=True, error_messages={'invalid':'Formato invalido'}, widget=forms.TextInput(attrs={'class': 'form-control', 'pattern':'[A-Za-z ]+'}))
    telefono = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    fecha_reserva = forms.DateTimeField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'date'}))
    hora = forms.TimeField(required=True, error_messages={'invalid':"Ingrese una hora valida"}, widget=forms.TimeInput(attrs={'class': 'form-control'}))
    cantidad_personas = forms.IntegerField(required=True, error_messages={'invalid':"Debes ingresar un numero"}, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    estado = forms.ChoiceField(required=True,choices=estados, widget=forms.Select(attrs={'class':'form-control'}))
    observacion = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = reservas
        fields = [
                'nombre', 
                'telefono', 
                'fecha_reserva', 
                'hora', 
                'cantidad_personas', 
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

    def clean_cantidad_personas(self):
        cantidad = self.cleaned_data.get('cantidad_personas')
        if cantidad >= 1 and cantidad<=15:
            return cantidad
        else:
            raise forms.ValidationError("Ingrese una cantidad entre 1 y 15")
            
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
