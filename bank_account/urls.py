from unicodedata import name
from django.urls import path
from .views import BankAccountListCreateAPIView


urlpatterns = [
        path('list-accounts/', BankAccountListCreateAPIView.as_view(), name='list_accounts'),
        ]
