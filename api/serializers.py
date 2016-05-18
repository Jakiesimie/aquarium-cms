import os
from rest_framework import serializers
from aquarium.models import Map, Tank, Habitat, Trivia, Species
from quiz.models import Grade, Quiz, Image, Test


# Quiz serializers
class QuizSerializer(serializers.ModelSerializer):
    # tank = serializers.StringRelatedField()
    images = serializers.StringRelatedField(many=True)
    # use_url - If set to False then filename string values will be used for the output representation.
    image_table_eng = serializers.ImageField(use_url=False)
    image_table_arabic = serializers.ImageField(use_url=False)

    class Meta:
        depth = 0
        model = Quiz
        fields = (
            'id', 'name', 'tank', 'grade', 'type', 'position', 'text_eng', 'text_arabic',
            'image_table_eng', 'image_table_arabic', 'images', 'created_at',
        )

class GradeSerializer(serializers.ModelSerializer):
    quiz_item = serializers.StringRelatedField(many=True)

    class Meta:
        model = Grade
        depth = 0
        fields = ('id', 'name', 'quiz_item')


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.StringRelatedField()

    class Meta:
        model = Image
        fields = ('id', 'image',)


class TestSerializer(serializers.ModelSerializer):
    image = serializers.StringRelatedField()

    class Meta:
        model = Test
        fields = ('id', 'image',)


# Aquarium
class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ('id', 'title', 'image', 'created_at', 'updated_at', 'is_current')


class TankSerializer(serializers.ModelSerializer):
    quiz_item = serializers.StringRelatedField(many=True) #, read_only=True)

    class Meta:
        model = Tank
        depth = 0
        fields = (
            'tank_id', 'habitat', 'name_eng', 'name_arabic', 'direction_label_eng',
            'direction_label_arabic', 'direction', 'quiz_item',
        )


class HabitatSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=False)

    class Meta:
        model = Habitat
        depth = 1
        fields = (
            'id', 'name_eng', 'name_arabic', 'image', 'description_eng',
            'description_arabic', 'trivia', 'knowledge_eng', 'knowledge_arabic'
        )


class TriviaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trivia
        fields = ('id', 'text_eng', 'text_arabic',)


class SpeciesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=False)
    # tank = serializers.StringRelatedField() #many=True)
    distribution_image = serializers.ImageField(use_url=False)

    class Meta:
        depth = 0
        model = Species
        fields = (
            'id', 'tank', 'name_eng', 'name_arabic', 'scientific_name', 'image', 'distribution_label_eng',
            'distribution_label_arabic', 'distribution_image', 'description_eng', 'description_arabic')

