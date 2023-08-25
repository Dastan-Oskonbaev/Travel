from django.contrib import admin

from .models import Favorite, FavoritePlaces, FavoriteAttractions, FavoriteHotels, FavoriteRestaurants


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
    )
    list_filter = (
        'customer',
    )
    list_display_links = (
        'customer',
    )
    search_fields = (
        'customer',
    )
    ordering = (
        'customer',
    )


@admin.register(FavoritePlaces)
class FavoritePlacesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'favorite',
        'place',
    )
    list_filter = (
        'favorite',
    )
    list_display_links = (
        'favorite',
    )
    search_fields = (
        'favorite',
    )
    ordering = (
        'favorite',
    )


@admin.register(FavoriteAttractions)
class FavoriteAttractionsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'favorite',
        'attraction',
    )
    list_filter = (
        'favorite',
    )
    list_display_links = (
        'favorite',
    )
    search_fields = (
        'favorite',
    )
    ordering = (
        'favorite',
    )


@admin.register(FavoriteHotels)
class FavoriteHotelsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'favorite',
        'hotel',
    )
    list_filter = (
        'favorite',
    )
    list_display_links = (
        'favorite',
    )
    search_fields = (
        'favorite',
    )
    ordering = (
        'favorite',
    )


@admin.register(FavoriteRestaurants)
class FavoriteRestaurantsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'favorite',
        'restaurant',
    )
    list_filter = (
        'favorite',
    )
    list_display_links = (
        'favorite',
    )
    search_fields = (
        'favorite',
    )
    ordering = (
        'favorite',
    )