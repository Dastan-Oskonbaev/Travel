from django.contrib import admin

from .models import (
    Region,
    WhatToTry,
    WhatToTryImage,
    Place,
    PlaceImage,
    Hotels,
    HotelsImage,
    Restaurants,
    RestaurantsImage,
    Events,
    EventsImage,
    Attractions,
    AttractionsImage,
)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'photo',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'id',
        'name',
        'description',
    )


@admin.register(WhatToTry)
class WhatToTryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'region',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'id',
        'name',
        'region',
        'description',
    )


@admin.register(WhatToTryImage)
class WhatToTryImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'what_to_try',
        'image',
    )
    list_display_links = (
        'what_to_try',
    )
    search_fields = (
        'id',
        'what_to_try',
    )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'region',
        'reviews',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'id',
        'name',
        'region',
        'reviews',
    )


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'place',
        'image',
    )
    list_display_links = (
        'place',
    )
    search_fields = (
        'id',
        'place',
        'image',
    )


@admin.register(Hotels)
class HotelsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'place',
        'reviews',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'id',
        'name',
        'place',
        'reviews',
    )


@admin.register(HotelsImage)
class HotelsImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'hotels',
        'image',
    )
    list_display_links = (
        'hotels',
    )
    search_fields = (
        'id',
        'hotels',
        'image',
    )


@admin.register(Restaurants)
class RestaurantsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'place',
        'price_range',
        'specialized_menu',
        'reviews',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'id',
        'name',
        'place',
        'price_range',
        'specialized_menu',
        'reviews',
    )


@admin.register(RestaurantsImage)
class RestaurantsImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'restaurants',
        'image',
    )
    list_display_links = (
        'restaurants',
    )
    search_fields = (
        'id',
        'restaurants',
        'image',
    )
