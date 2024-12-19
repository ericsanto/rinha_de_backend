from sys import exception
from django.db.models.deletion import models
from django.http.request import validate_host
from rest_framework import serializers
from .models import BankAccount
from client.models import ClientUser
from django.core.exceptions import ValidationError


class BankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankAccount
        fields = ['client_cpf', 'client', 'account_number', 'balance']
        read_only_fields = ['account_number', 'balance', 'client']
    
    def validate(self, data):

        print(data['client_cpf'])
        
        try:
            user = ClientUser.objects.get(cpf=data['client_cpf'])
        except ClientUser.DoesNotExist:
            raise ValidationError({'error': 'Cliente não encontrado',
                                   'detail': 'Não foi encontrado um cliente com o CPF fornecido. Por favor, cadastre-se primeiro para abrir uma conta.'})
        
        data['client'] = user
        
        return data
