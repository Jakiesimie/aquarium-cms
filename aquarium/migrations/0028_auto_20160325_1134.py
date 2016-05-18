# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 11:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aquarium', '0027_tank_tank_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='tank',
            field=models.ForeignKey(db_column='tank_id', on_delete=django.db.models.deletion.CASCADE, to='aquarium.Tank'),
        ),
    ]