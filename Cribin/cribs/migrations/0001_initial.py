# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 10:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=254)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=254)),
                ('postal_num', models.CharField(max_length=10)),
                ('postal_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Crib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_rooms', models.PositiveSmallIntegerField()),
                ('description', models.TextField(blank=True)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cribs.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('last_name', models.CharField(max_length=50)),
                ('fist_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=b'')),
                ('gender', models.CharField(max_length=1)),
                ('birth_date', models.DateField()),
                ('min_number_of_cribmates', models.PositiveSmallIntegerField()),
                ('max_number_of_cribmates', models.PositiveSmallIntegerField()),
                ('min_price', models.PositiveSmallIntegerField()),
                ('max_price', models.PositiveSmallIntegerField()),
                ('desiredLocation', models.CharField(max_length=100)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cribs.Address')),
            ],
        ),
    ]
