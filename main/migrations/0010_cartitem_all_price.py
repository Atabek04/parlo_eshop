# Generated by Django 4.1.2 on 2022-10-30 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_cart_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='all_price',
            field=models.FloatField(default=0),
        ),
    ]
