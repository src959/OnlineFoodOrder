# Generated by Django 2.2 on 2021-06-11 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
        ('pwn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('total', models.FloatField()),
                ('status', models.CharField(max_length=30)),
                ('date', models.DateField(auto_now_add=True)),
                ('address', models.TextField()),
                ('items', models.ManyToManyField(to='vendor.FoodItemsModel')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('contact', models.IntegerField(unique=True)),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=20)),
                ('OTP', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pwn.CityModel')),
            ],
        ),
    ]