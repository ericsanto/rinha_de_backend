from http import client
from django.shortcuts import render
from rest_framework.exceptions import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import Response
from rest_framework.schemas.coreapi import serializers
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .models import BankAccount
from .serializers import BankAccountSerializer


class BankAccountListCreateAPIView(ListCreateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer


    def post(self, request, *args, **kwargs):
       
        cpf_client = request.data.get('client_cpf') 

        try:
            account = BankAccount.objects.get(client_cpf=cpf_client)
            return Response({"detail": "Esse CPF ja tem uma conta vinculada"}, status=status.HTTP_400_BAD_REQUEST)
        
        except:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({"detail": "Conta criada com sucesso"}, status=status.HTTP_201_CREATED)
            
            


