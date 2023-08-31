from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import CultureCategory, Culture


@admin.register(CultureCategory)
class CultureCategoryAdmin(TranslationAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name',)
    search_fields = ('name', 'description')
    list_filter = ('name', 'description')
    ordering = ('name',)


@admin.register(Culture)
class CultureAdmin(TranslationAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name', 'description')
    list_filter = ('name',)
    ordering = ('name',)

