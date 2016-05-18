# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 08:19
from __future__ import unicode_literals

import aquarium.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_eng', models.CharField(max_length=200)),
                ('name_arabic', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to=aquarium.models.upload_to)),
                ('description_eng', models.TextField()),
                ('description_arabic', models.TextField()),
                ('knowledge_eng', models.TextField()),
                ('knowledge_arabic', models.TextField()),
            ],
            options={
                'verbose_name': 'Habitat',
                'verbose_name_plural': 'Habitats',
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('map', models.ImageField(blank=True, null=True, upload_to=aquarium.models.upload_to)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Map',
                'verbose_name_plural': 'Maps',
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_eng', models.CharField(max_length=200)),
                ('name_arabic', models.CharField(max_length=200)),
                ('scientific_name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to=aquarium.models.upload_to)),
                ('distribution_label_eng', models.CharField(max_length=200)),
                ('distribution_label_arabic', models.CharField(max_length=200)),
                ('distribution_image', models.ImageField(blank=True, null=True, upload_to=aquarium.models.upload_to)),
                ('description_eng', models.TextField()),
                ('description_arabic', models.TextField()),
            ],
            options={
                'verbose_name': 'Species',
                'verbose_name_plural': 'Species',
            },
        ),
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_eng', models.CharField(max_length=200)),
                ('name_arabic', models.CharField(max_length=200)),
                ('direction_label_eng', models.CharField(max_length=200)),
                ('direction_label_arabic', models.CharField(max_length=200)),
                ('direction', models.IntegerField(choices=[(0, 'Up'), (1, 'Down'), (2, 'Left'), (3, 'Right')], default='Up')),
                ('habitat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aquarium.Habitat')),
            ],
            options={
                'verbose_name': 'Tank',
                'verbose_name_plural': 'Tanks',
            },
        ),
        migrations.AddField(
            model_name='species',
            name='tank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aquarium.Tank'),
        ),
    ]
