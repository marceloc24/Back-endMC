from rest_framework import serializers
from seminarioApp.models import Inscritos, Institucion

class InscritosSerial(serializers.ModelSerializer):
    class Meta:
        model = Inscritos
        fields = '__all__'

class InstitucionSerial(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'