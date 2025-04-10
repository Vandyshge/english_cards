from django.shortcuts import render, redirect
from .models import Card, Lesson
from .forms import CardForm, LessonForm
from django.contrib import messages

def home(request):
    return render(request, 'cards/home.html')

def card_list(request):
    cards = Card.objects.all().order_by('-created_at')
    return render(request, 'cards/card_list.html', {'cards': cards})

def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Карточка успешно добавлена!')
            return redirect('card_list')
    else:
        form = CardForm()
    return render(request, 'cards/add_card.html', {'form': form})

def lesson_list(request):
    lessons = Lesson.objects.all().order_by('-created_at')
    return render(request, 'cards/lesson_list.html', {'lessons': lessons})

def add_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Урок успешно создан!')
            return redirect('lesson_list')
    else:
        form = LessonForm()
    return render(request, 'cards/add_lesson.html', {'form': form})

def practice(request):
    cards = Card.objects.all().order_by('?')[:10]  # 10 случайных карточек
    return render(request, 'cards/practice.html', {'cards': cards})