# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 14:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aquarium', '0023_auto_20160320_1218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tank',
            options={'ordering': ['id'], 'verbose_name': 'Tank', 'verbose_name_plural': 'Tanks'},
        ),
    ]
