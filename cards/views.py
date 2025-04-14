from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request, 'cards/lesson_list.html', {
        'lessons': lessons,
        'can_delete': request.user.is_authenticated
    })

def add_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, f'Урок "{lesson.title}" успешно создан!')
            return redirect('lesson_list')
        else:
            print("Форма невалидна:", form.errors)
            messages.error(request, 'Исправьте ошибки в форме')
    else:
        form = LessonForm()
    
    return render(request, 'cards/add_lesson.html', {'form': form})

def practice(request):
    cards = Card.objects.all().order_by('?')[:5]
    return render(request, 'cards/practice.html', {'cards': cards})

def delete_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        lesson_pk = card.lesson.pk  # Сохраняем ID урока перед удалением
        card.delete()
        messages.success(request, 'Карточка успешно удалена!')
        return redirect('lesson_cards', pk=lesson_pk)  # Перенаправляем обратно в урок
    
    return render(request, 'cards/confirm_delete.html', {
        'object': card,
        'type': 'карточку',
        'back_url': 'lesson_cards',
        'back_kwargs': {'pk': card.lesson.pk}
    })

def delete_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        lesson.delete()
        messages.success(request, f'Урок "{lesson.title}" успешно удалён!')
        return redirect('lesson_list')
    
    return render(request, 'cards/confirm_delete.html', {
        'object': lesson,
        'type': 'урок',
        'back_url': 'lesson_list'
    })

def lesson_cards(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    cards = lesson.cards.all().order_by('-created_at')
    return render(request, 'cards/lesson_cards.html', {'cards': cards, 'lesson': lesson})

def practice_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    cards = lesson.cards.all().order_by('?')
    
    if not cards.exists():
        messages.warning(request, "В этом уроке нет карточек для тренировки!")
        return redirect('lesson_cards', pk=pk)
    
    return render(request, 'cards/practice.html', {
        'cards': cards,
        'lesson': lesson
    })