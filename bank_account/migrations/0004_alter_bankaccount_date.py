# Generated by Django 5.1.4 on 2024-12-19 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account', '0003_bankaccount_client_cpf_alter_bankaccount_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]