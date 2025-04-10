# Generated by Django 5.2 on 2025-04-10 20:51

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)])),
                ('translation', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('example', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='cards/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='cards.lesson')),
            ],
        ),
    ]
