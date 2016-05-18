# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
from django.conf import settings
from django.db import models
# from tinymce.models import HTMLField


def upload_to(instance, filename):
    return '/'.join(['quiz', str(filename)])

def upload_to_test(instance, filename):
    return str(filename)


class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'

    def __unicode__(self):
        return '{}: {}'.format(self.id, self.name)


class Quiz(models.Model):
    item_types = (
        ('text', 'text'),
        ('image', 'image'),
        ('image_table', 'image_table'),
    )

    items_order = tuple((n+1, m) for n,m in enumerate(xrange(1,16)))

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    tank = models.ForeignKey('aquarium.Tank', to_field='tank_id', related_name='quiz_item')
    grade = models.ForeignKey('quiz.Grade', related_name='quiz_item')
    type = models.CharField(max_length=11, choices=item_types)
    position = models.IntegerField(choices=items_order)
    text_eng = models.TextField(null=True, blank=True)
    text_arabic = models.TextField(null=True, blank=True)
    image_table_eng = models.ImageField(upload_to=upload_to, null=True, blank=True)
    image_table_arabic = models.ImageField(upload_to=upload_to, null=True, blank=True)
    images = models.ManyToManyField('quiz.Image', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{}: {}'.format(self.id, self.name)

    class Meta:
        ordering = ['id']
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to=upload_to, null=True, blank=True)

    def image_tag(self):
        return '<a href="{0}" target="_blank"><img src="{0}" width="100"></a>'.format(
            self.image.url) if self.image else '-'

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __unicode__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'Quiz Image'
        verbose_name_plural = 'Quiz Images'


class Test(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Testing'
        verbose_name_plural = 'Testing'

    def __unicode__(self):
        return self.text