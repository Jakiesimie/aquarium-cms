# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aquarium', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='is_current',
            field=models.BooleanField(default=False),
        ),
    ]
