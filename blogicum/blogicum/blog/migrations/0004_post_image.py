# Generated by Django 3.2.16 on 2024-12-11 16:45

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20241207_0433'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=pathlib.PureWindowsPath('D:/Development/university/ya-practicum-backend/blogicum/media/post_images'), verbose_name='Изображение'),
        ),
    ]