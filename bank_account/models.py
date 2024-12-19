from django.db import models
import random
from django.core.validators import MinValueValidator
from django.db.models.fields import validators
from client.models import ClientUser
from bank.models import Bank

class BankAccount(models.Model):
    client = models.ForeignKey(ClientUser, on_delete=models.CASCADE, related_name='client_data')
    client_cpf = models.CharField(max_length=14)
    account_number = models.CharField(max_length=12, unique=True)
    balance = models.DecimalField(decimal_places=2, default=0, max_digits=10,validators=[MinValueValidator(0)])
    date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self) -> str:
        return self.account_number

    
    def save(self, *args, **kwargs):
        code_bank = "001"
        numbers = []

        for i in range(0,4):
            index = random.randint(0,12)
            if len(numbers) == 5:
                break
            numbers.append(index)

        
        number_string = ''.join(code_bank + str(number) for number in numbers)

        print(number_string)
        self.account_number = number_string
        super(BankAccount, self).save(*args, **kwargs) 

