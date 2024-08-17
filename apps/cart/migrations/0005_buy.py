# Generated by Django 5.1 on 2024-08-17 17:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_delete_buy'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total price of all products')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Payment verification')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('products', models.ManyToManyField(to='cart.product', verbose_name='Purchased products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Purchase user')),
            ],
            options={
                'verbose_name': 'Buy',
                'verbose_name_plural': 'Buys',
            },
        ),
    ]
