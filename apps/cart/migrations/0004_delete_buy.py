# Generated by Django 5.1 on 2024-08-17 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_buy_owner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Buy',
        ),
    ]