from django import forms
from models import Map, Tank, Habitat, Trivia, Species

class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = [
            'title',
            'image',
            'is_current',
        ]


class TankForm(forms.ModelForm):
    class Meta:
        model = Tank
        fields = [
            'tank_id',
            'name_eng',
            'name_arabic',
            'habitat',
            'direction_label_eng',
            'direction_label_arabic',
            'direction',
        ]


class HabitatForm(forms.ModelForm):
    class Meta:
        model = Habitat
        fields = [
            'name_eng',
            'name_arabic',
            'image',
            'description_eng',
            'description_arabic',
            'knowledge_eng',
            'knowledge_arabic',
        ]


class TriviaForm(forms.ModelForm):
    class Meta:
        model = Trivia
        fields = [
            'name',
            'text_eng',
            'text_arabic',
        ]


class SpeciesForm(forms.ModelForm):
    class Meta:
        model = Species
        fields = [
            'name_eng',
            'name_arabic',
            'scientific_name',
            'image',
            'distribution_label_eng',
            'distribution_label_arabic',
            'distribution_image',
            'description_eng',
            'description_arabic',
        ]
