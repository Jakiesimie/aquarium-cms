# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 20:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0044_remove_quiz_tank'),
        ('aquarium', '0015_auto_20160319_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='tank',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz'),
            preserve_default=False,
        ),
    ]
