# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20160315_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizimage',
            name='quiz_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_item', to='quiz.QuizItem'),
        ),
    ]
