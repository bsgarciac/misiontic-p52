from django.shortcuts import render
from rest_framework import views, generics, authentication, permissions, status
from .serializers import PersonaSoporteSerializer, PQRSerializer, BankSerializer, UserSerializer, UserCreationSerializer
from .models import PersonaSoporte, PQR, Bank
from rest_framework.response import Response
from django.contrib.auth.models import User


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


class BankListCreate(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class UserRetrieve(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user) 
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserCreate(views.APIView):
    def post(self, request):
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            PersonaSoporte.objects.create(user=user, edad=request.data['edad'])
            return Response(status=status.HTTP_201_CREATED)
