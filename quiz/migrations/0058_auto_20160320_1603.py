# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0057_auto_20160320_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]