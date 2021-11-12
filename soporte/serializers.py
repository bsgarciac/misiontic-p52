from rest_framework import serializers
from .models import PQR, PersonaSoporte, Bank
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class PersonaSoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaSoporte
        fields = '__all__'


class PQRSerializer(serializers.ModelSerializer):
    persona_soporte = PersonaSoporteSerializer(read_only=True)

    class Meta:
        model = PQR
        fields = ['persona_soporte', 'estado', 'comentario', 'created']


class BankSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Bank
        fields = ['users', 'name']