from django.contrib import admin

from .models import Review, Rating, RestaurantRating


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
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
    )
    list_per_page = 25
    ordering = ('-id',)
    readonly_fields = ('id',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'content_object',
    )
    list_display_links = (
        'id',
        'user',
    )
    search_fields = (
        'user',
        'content_object',
        'rating_value',
    )
    list_filter = (
        'user',
    )
    list_per_page = 25
    ordering = ('-id',)
    readonly_fields = ('id',)


@admin.register(RestaurantRating)
class RestaurantRatingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'restaurant',
        'rating',
        'nutrition',
        'service',
        'price_quality',
        'atmosphere',
    )
    list_display_links = (
        'user',
    )
    search_fields = (
        'user',
        'restaurant',
        'rating',
    )
    list_filter = (
        'user',
    )
    list_per_page = 25
    ordering = ('-id',)
