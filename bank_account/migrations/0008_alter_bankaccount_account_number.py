# Generated by Django 5.1.4 on 2024-12-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account', '0007_remove_bankaccount_bank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='account_number',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]