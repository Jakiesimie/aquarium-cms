# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import quiz.models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizitem',
            name='image',
            field=models.FileField(upload_to=quiz.models.upload_to),
        ),
    ]