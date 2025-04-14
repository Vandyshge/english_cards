"""
URL configuration for english_tutor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cards import views
from django.conf import settings
from django.conf.urls.static import static

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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)