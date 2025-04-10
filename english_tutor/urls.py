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
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cards/', views.card_list, name='card_list'),
    path('cards/add/', views.add_card, name='add_card'),
    path('lessons/', views.lesson_list, name='lesson_list'),
    path('lessons/add/', views.add_lesson, name='add_lesson'),
    path('practice/', views.practice, name='practice'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)