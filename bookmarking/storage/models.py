from django.db import models


TYPES = (
    ('website', 'website'),
    ('book', 'book'),
    ('article', 'article'),
    ('music', 'music'),
    ('video', 'video'),
)


class Bookmark(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок страницы'
    )
    description = models.TextField(
        verbose_name='Краткое описание',
        blank=True,
        null=True
    )
    url = models.URLField(
        verbose_name='Ссылка',
        unique=True,
        blank=False
    )
    type = models.CharField(
        choices=TYPES,
        default='website',
        verbose_name='Тип контента',
        max_length=256
    )
    image = models.URLField(
        blank=True,
        null=True,
        verbose_name='Ссылка на превью'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Обновлено'
    )


class BMCollection(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название коллекции'
    )
    description = models.TextField(
        verbose_name='Краткое описание'
    )
    bookmarks = models.ManyToManyField(
        Bookmark,
        verbose_name='Закладки'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Обновлено'
    )
