from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=255)
    bank_code = models.CharField(max_length=255)

    def __str__(self):
        return self.name
