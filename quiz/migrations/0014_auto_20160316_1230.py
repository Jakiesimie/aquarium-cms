# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 12:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_auto_20160316_1211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizitem',
            old_name='grade',
            new_name='grade_name',
        ),
        migrations.AddField(
            model_name='grade',
            name='quizitems',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.QuizItem'),
            preserve_default=False,
        ),
    ]
