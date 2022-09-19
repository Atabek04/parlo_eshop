# Generated by Django 3.2.12 on 2022-09-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('code', models.CharField(blank=True, max_length=50)),
                ('level', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('code', models.CharField(blank=True, max_length=50)),
                ('level', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
