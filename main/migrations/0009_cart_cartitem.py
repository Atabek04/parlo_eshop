# Generated by Django 4.1.2 on 2022-10-24 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20220917_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=200)),
                ('last_name', models.CharField(blank=True, max_length=200)),
                ('first_name', models.CharField(blank=True, max_length=200)),
                ('zip_code', models.CharField(blank=True, max_length=200)),
                ('country', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('person', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=200)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('is_accepted', models.BooleanField(default=False)),
                ('is_payed', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=0)),
                ('session_id', models.CharField(blank=True, max_length=200)),
                ('amount', models.IntegerField(default=1)),
                ('discount', models.IntegerField(default=0)),
                ('orig_price', models.FloatField(default=0)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('price', models.FloatField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cart')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.good')),
            ],
        ),
    ]