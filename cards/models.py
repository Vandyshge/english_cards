from django.db import models
from django.core.validators import MinLengthValidator

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Card(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='cards')
    word = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    translation = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    example = models.TextField(blank=True)
    image = models.ImageField(upload_to='cards/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.word} - {self.translation}"