from django.contrib import admin

from .models import Bookmark, BMCollection


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'created_at', 'updated_at')


@admin.register(BMCollection)
class BMCollectionAdmin(admin.ModelAdmin):
    pass
