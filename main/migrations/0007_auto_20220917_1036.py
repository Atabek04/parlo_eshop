# Generated by Django 3.2.12 on 2022-09-17 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20220907_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
        ),
        migrations.AddField(
            model_name='size',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
        ),
    ]
