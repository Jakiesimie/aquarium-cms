# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0059_auto_20160321_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='image',
        ),
        migrations.AddField(
            model_name='test',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]