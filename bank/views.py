from django.db.models import query
from django.shortcuts import render
from bank import serializers
from rest_framework import generics
from .serializers import BankSerializer
from .models import Bank


class BankListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

