# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 12:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0016_auto_20160316_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grade',
            old_name='tank_name',
            new_name='tank',
        ),
    ]