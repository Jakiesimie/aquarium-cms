# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0065_auto_20160325_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='tank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_item', to='aquarium.Tank', to_field='tank_id'),
        ),
    ]
