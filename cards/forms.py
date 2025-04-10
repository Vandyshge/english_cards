from django import forms
from .models import Card, Lesson

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['lesson', 'word', 'translation', 'example', 'image']
        widgets = {
            'example': forms.Textarea(attrs={'rows': 3}),
        }

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }