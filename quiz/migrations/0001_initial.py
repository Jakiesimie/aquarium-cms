# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 08:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import quiz.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aquarium', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Grade Category',
                'verbose_name_plural': 'Grade Categories',
            },
        ),
        migrations.CreateModel(
            name='QuizItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('text_eng', models.TextField(blank=True, null=True)),
                ('text_arabic', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=quiz.models.upload_to)),
                ('item_type', models.CharField(choices=[('image', 'image'), ('text', 'text')], max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Grade')),
                ('tank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aquarium.Tank')),
            ],
            options={
                'verbose_name': 'Quiz Item',
                'verbose_name_plural': 'Quiz Items',
            },
        ),
    ]
