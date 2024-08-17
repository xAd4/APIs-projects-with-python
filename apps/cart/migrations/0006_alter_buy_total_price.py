# Generated by Django 5.1 on 2024-08-17 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_buy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total price of all products'),
        ),
    ]
