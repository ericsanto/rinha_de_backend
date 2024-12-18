from unicodedata import name
from django.urls import path
from .views import BankListCreateAPIView

urlpatterns = [
        path('list-banks', BankListCreateAPIView.as_view(), name='list_banks')
        ]
