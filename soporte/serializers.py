from rest_framework import serializers
from .models import PQR, PersonaSoporte

class PersonaSoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaSoporte
        fields = '__all__'


class PQRSerializer(serializers.ModelSerializer):
    persona_soporte = PersonaSoporteSerializer(read_only=True)

    class Meta:
        model = PQR
        fields = ['persona_soporte', 'estado', 'comentario', 'created']