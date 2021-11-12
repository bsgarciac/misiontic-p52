from django.urls import path
from .views import PersonaSoporteListCreate, PersonaSoporteUpdateDelete, PQRListCreate, PQRUpdateDelete, BankListCreate, BankUpdateDelete

urlpatterns = [
    path('personas-soporte/', PersonaSoporteListCreate.as_view()),
    path('personas-soporte/<pk>/', PersonaSoporteUpdateDelete.as_view()),
    path('pqr/', PQRListCreate.as_view()),
    path('pqr/<pk>/', PQRUpdateDelete.as_view()),
    path('bank/', BankListCreate.as_view()),
    path('bank/<pk>/', BankUpdateDelete.as_view())
]