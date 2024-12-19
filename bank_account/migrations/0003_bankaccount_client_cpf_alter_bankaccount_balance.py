# Generated by Django 5.1.4 on 2024-12-18 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account', '0002_alter_bankaccount_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='client_cpf',
            field=models.CharField(default=1, max_length=14),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='balance',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
