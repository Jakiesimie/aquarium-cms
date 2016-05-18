# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator
# from tinymce.models import HTMLField


def upload_to(instance, filename):
    return '/'.join(['aquarium', str(filename)])


class Map(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_current = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Map'
        verbose_name_plural = 'Maps'

    def image_tag(self):
        # print 'PATH:', self.image
        return '<a href="{0}" target="_blank"><img src="{0}" width="200"></a>'.format(
            self.image.url) if self.image else '-'

    image_tag.short_description = 'Map'
    image_tag.allow_tags = True


class Tank(models.Model):
    DIRECTIONS = (
        (0, 'Up'),
        (1, 'Down'),
        (2, 'Left'),
        (3, 'Right'),
        )

    id = models.AutoField(primary_key=True)
    tank_id = models.IntegerField(unique=True, null=True, blank=True, validators=[MinValueValidator(1)]) # min value added after shipment
    name_eng = models.CharField(max_length=200)
    name_arabic = models.CharField(max_length=200)
    habitat = models.ForeignKey('aquarium.Habitat')
    direction_label_eng = models.CharField(max_length=200)
    direction_label_arabic = models.CharField(max_length=200)
    direction = models.IntegerField(choices=DIRECTIONS, default='Up')

    class Meta:
        verbose_name = 'Tank'
        verbose_name_plural = 'Tanks'

    def __unicode__(self):
        return self.name_eng


class Habitat(models.Model):
    id = models.AutoField(primary_key=True)
    name_eng = models.CharField(max_length=200)
    name_arabic = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    description_eng = models.TextField()
    description_arabic = models.TextField()
    trivia = models.ManyToManyField('aquarium.Trivia')
    knowledge_eng = models.TextField()
    knowledge_arabic = models.TextField()

    def __unicode__(self):
        return self.name_eng

    class Meta:
        verbose_name = 'Habitat'
        verbose_name_plural = 'Habitats'

    def image_tag(self):
        # print 'PATH:', self.image
        return '<a href="{0}" target="_blank"><img src="{0}" width="200"></a>'.format(
            self.image.url) if self.image else '-'

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class Trivia(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    text_eng = models.TextField(null=True, blank=True)
    text_arabic = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Trivia'
        verbose_name_plural = 'Trivia'


class Species(models.Model):
    id = models.AutoField(primary_key=True)
    tank = models.ForeignKey('aquarium.Tank', to_field='tank_id')
    name_eng = models.CharField(max_length=200)
    name_arabic = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    distribution_label_eng = models.CharField(max_length=200)
    distribution_label_arabic = models.CharField(max_length=200)
    distribution_image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    description_eng = models.TextField()
    description_arabic = models.TextField()

    def __unicode__(self):
        return '{1} ({0})'.format(self.name_eng, self.name_arabic)

    class Meta:
        verbose_name = 'Species'
        verbose_name_plural = 'Species'

    def image_tag(self):
        # print 'PATH:', self.image
        return '<a href="{0}" target="_blank"><img src="{0}" width="150"></a>'.format(
            self.image.url) if self.image else '-'

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def distribution_image_tag(self):
        # print 'PATH:', self.distribution_image
        return '<a href="{0}" target="_blank"><img src="{0}" width="100"></a>'.format(
            self.distribution_image.url) if self.distribution_image else '-'

    distribution_image_tag.short_description = 'Distribution Image'
    distribution_image_tag.allow_tags = True


