# Generated by Django 4.2.2 on 2023-08-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_alter_transactioncatalogue_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.FloatField(default=0),
        ),
    ]