# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 14:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0052_auto_20160320_1218'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuizImage',
            new_name='Image',
        ),
    ]
