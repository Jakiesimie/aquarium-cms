# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0048_auto_20160320_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='tank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_item', to='aquarium.Tank'),
        ),
    ]