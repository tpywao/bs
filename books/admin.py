from django.contrib import admin
from django.utils.html import format_html

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'thumbnail',
        'isbn',
        'stock',
        'title',
        'author',
        'published_date',
        )
    fields = (
        'isbn',
        'stock',
        'title',
        'author',
        'published_date',
        )

    def thumbnail(self, obj):
        print(obj)
        return format_html(
            '<img src="{}"></img>',
            obj.thumbnail_url
            )
    thumbnail.short_description = 'サムネイル'
