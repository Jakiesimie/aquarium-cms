# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 14:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20160315_1334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quizimage',
            options={'ordering': ['quizitem'], 'verbose_name': 'Quiz Image', 'verbose_name_plural': 'Quiz Images'},
        ),
        migrations.RenameField(
            model_name='quizimage',
            old_name='quiz_item',
            new_name='quizitem',
        ),
        migrations.RenameField(
            model_name='quiztext',
            old_name='quiz_item',
            new_name='quizitem',
        ),
        migrations.AlterUniqueTogether(
            name='quizimage',
            unique_together=set([('quizitem',)]),
        ),
    ]
