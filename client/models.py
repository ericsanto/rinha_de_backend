from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser


class ClientUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    
    REQUIRED_FIELDS = ["date_of_birth", "first_name", "last_name", "cpf", "email", "address"]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

