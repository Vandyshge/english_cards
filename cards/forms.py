from django import forms
from .models import Card, Lesson
import re

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['lesson', 'word', 'translation', 'example', 'image']
        widgets = {
            'example': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_word(self):
        word = self.cleaned_data['word']
        if not re.match(r'^[a-zA-Z]+$', word):
            raise forms.ValidationError("Слово должно содержать только буквы английского алфавита")
        return word

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})