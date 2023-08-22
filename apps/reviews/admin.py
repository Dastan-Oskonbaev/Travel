from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'rating',
        'author',
        'content_object',
    )
    list_display_links = (
        'id',
        'author',
    )
    search_fields = (
        'author',
        'content_object',
        'text',
    )
    list_filter = (
        'author',
        'rating',
    )
    list_per_page = 25
    ordering = ('-id',)
    readonly_fields = ('id',)
