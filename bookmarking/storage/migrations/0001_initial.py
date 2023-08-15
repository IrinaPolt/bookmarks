# Generated by Django 4.2.4 on 2023-08-15 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок страницы')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Краткое описание')),
                ('url', models.URLField(unique=True, verbose_name='Ссылка')),
                ('type', models.CharField(choices=[('website', 'website'), ('book', 'book'), ('article', 'article'), ('music', 'music'), ('video', 'video')], default='website', max_length=256, verbose_name='Тип контента')),
                ('image', models.URLField(blank=True, null=True, verbose_name='Ссылка на превью')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
        ),
        migrations.CreateModel(
            name='BMCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название коллекции')),
                ('description', models.TextField(verbose_name='Краткое описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('bookmarks', models.ManyToManyField(to='storage.bookmark', verbose_name='Закладки')),
            ],
        ),
    ]
