# Generated by Django 5.1.7 on 2025-03-15 22:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('height', models.IntegerField(verbose_name='Высота над уровнем моря')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('last_name', models.CharField(max_length=256, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=256, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=256, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=11, verbose_name='Номер телефона')),
            ],
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('NE', 'new'), ('PE', 'pending'), ('AC', 'accepted'), ('RE', 'rejected')], default='NE', max_length=2, verbose_name='Статус')),
                ('beauty_title', models.CharField(max_length=256, verbose_name='Тип местности')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('other_titles', models.CharField(max_length=256, verbose_name='Другие названия')),
                ('connect', models.TextField(blank=True, verbose_name='Сопроводительный текст')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('level_spring', models.CharField(blank=True, max_length=5, verbose_name='Уровень сложности весной')),
                ('level_summer', models.CharField(blank=True, max_length=5, verbose_name='Уровень сложности летом')),
                ('level_autumn', models.CharField(blank=True, max_length=5, verbose_name='Уровень сложности осенью')),
                ('level_winter', models.CharField(blank=True, max_length=5, verbose_name='Уровень сложности зимой')),
                ('coords', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pereval.coords')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.user')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.URLField()),
                ('title', models.CharField(blank=True, max_length=256, verbose_name='Примечание')),
                ('datetime', models.DateField(auto_now_add=True)),
                ('pereval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pereval.pereval')),
            ],
        ),
    ]
