# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 11:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aquarium', '0003_auto_20160315_1326'),
        ('quiz', '0010_auto_20160315_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizitem',
            name='tank',
        ),
        migrations.AddField(
            model_name='grade',
            name='tank',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='related_grade', to='aquarium.Tank'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quizimage',
            name='quiz_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_quiz_image', to='quiz.QuizItem'),
        ),
        migrations.AlterField(
            model_name='quizitem',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_quiz_item', to='quiz.Grade'),
        ),
        migrations.AlterField(
            model_name='quiztext',
            name='quiz_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_quiz_text', to='quiz.QuizItem'),
        ),
        migrations.AlterUniqueTogether(
            name='quiztext',
            unique_together=set([('quiz_item',)]),
        ),
    ]
