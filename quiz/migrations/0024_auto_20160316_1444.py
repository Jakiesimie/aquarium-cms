# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import quiz.models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0023_auto_20160316_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizImageArabic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image_arabic', models.ImageField(blank=True, null=True, upload_to=quiz.models.upload_to)),
                ('quiz_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_image_arabic', to='quiz.QuizItem')),
            ],
            options={
                'ordering': ['quiz_item'],
                'verbose_name': 'Quiz Image (Arabic)',
                'verbose_name_plural': 'Quiz Images (Arabic)',
            },
        ),
        migrations.RemoveField(
            model_name='quizimage',
            name='image_arabic',
        ),
        migrations.AlterUniqueTogether(
            name='quizimagearabic',
            unique_together=set([('quiz_item',)]),
        ),
    ]
