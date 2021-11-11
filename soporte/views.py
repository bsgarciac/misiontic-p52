from django.shortcuts import render
from rest_framework import generics
from .serializers import PersonaSoporteSerializer, PQRSerializer
from .models import PersonaSoporte, PQR

# Create your views here.

class PersonaSoporteListCreate(generics.ListCreateAPIView):
    queryset = PersonaSoporte.objects.all()
    serializer_class = PersonaSoporteSerializer

class PersonaSoporteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonaSoporte.objects.all()
    serializer_class = PersonaSoporteSerializer

class PQRListCreate(generics.ListCreateAPIView):
    queryset = PQR.objects.all()
    serializer_class = PQRSerializer

class PQRUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PQR.objects.all()
    serializer_class = PQRSerializer