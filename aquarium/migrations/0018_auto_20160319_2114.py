# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0044_remove_quiz_tank'),
        ('aquarium', '0017_auto_20160319_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tank',
            name='quiz',
        ),
        migrations.AddField(
            model_name='tank',
            name='tank_quiz',
            field=models.ManyToManyField(related_query_name='tag', to='quiz.Quiz'),
        ),
    ]
