from django import forms
from models import Quiz, Image


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = [
            'grade',
            'type',
            'position',
        ]

class QuizTextForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = [
            'position',
            'grade',
            'text_eng',
            'text_arabic'
        ]


class QuizImageForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = [
            'position',
            'grade',
        ]

class QuizTableForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = [
            'position',
            'grade',
            'image_table_eng',
            'image_table_arabic',
        ]

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']

