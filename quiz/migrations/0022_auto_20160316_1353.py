# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0021_auto_20160316_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiztext',
            name='text_arabic',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quiztext',
            name='text_eng',
            field=models.TextField(blank=True, null=True),
        ),
    ]
