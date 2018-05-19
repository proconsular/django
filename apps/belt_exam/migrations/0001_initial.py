# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-18 16:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('fromDate', models.DateTimeField()),
                ('toDate', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_trips', to='belt_exam.User'),
        ),
        migrations.AddField(
            model_name='trip',
            name='joined_users',
            field=models.ManyToManyField(related_name='joined_trips', to='belt_exam.User'),
        ),
    ]
