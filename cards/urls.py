from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cards/', views.card_list, name='card_list'),
    path('cards/add/', views.add_card, name='add_card'),
    path('cards/delete/<int:pk>/', views.delete_card, name='delete_card'),
    path('lessons/', views.lesson_list, name='lesson_list'),
    path('lessons/add/', views.add_lesson, name='add_lesson'),
    path('lessons/delete/<int:pk>/', views.delete_lesson, name='delete_lesson'),
    path('lessons/<int:pk>/cards/', views.lesson_cards, name='lesson_cards'),
    path('practice/', views.practice, name='practice'),
    path('practice/lesson/<int:pk>/', views.practice_lesson, name='practice_lesson'),
]