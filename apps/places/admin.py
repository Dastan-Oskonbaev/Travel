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
    Attractions,
    AttractionsImage, EventsCategory,
)


class WhatToTryImageInline(admin.TabularInline):
    model = WhatToTryImage
    extra = 1


class WhatToTryInline(admin.TabularInline):
    model = WhatToTry
    extra = 1


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
    inlines = [
        WhatToTryInline,
    ]


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
    inlines = [
        WhatToTryImageInline,
    ]


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


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'id',
        'name',
        'description',
    )
    inlines = [
        PlaceImageInline,
    ]


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


class HotelsImageInline(admin.TabularInline):
    model = HotelsImage
    extra = 1


@admin.register(Hotels)
class HotelsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'place',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'id',
        'name',
        'place',
    )
    inlines = [
        HotelsImageInline,
    ]


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


class RestaurantsImageInline(admin.TabularInline):
    model = RestaurantsImage
    extra = 1


@admin.register(Restaurants)
class RestaurantsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'place',
        'price_range',
        'specialized_menu',
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
    )
    inlines = [
        RestaurantsImageInline,
    ]


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


@admin.register(EventsCategory)
class EventsCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'id',
        'name',
    )


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'place',
        'category',
        'date',
        'address',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'id',
        'name',
        'place',
        'category',
        'date',
        'address',
    )


class AttractionsImageInline(admin.TabularInline):
    model = AttractionsImage
    extra = 1


@admin.register(Attractions)
class AttractionsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'place',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'id',
        'name',
        'place',
    )
    inlines = [
        AttractionsImageInline,
    ]


@admin.register(AttractionsImage)
class AttractionsImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'attractions',
        'image',
    )
    list_display_links = (
        'attractions',
    )
    search_fields = (
        'id',
        'attractions',
        'image',
    )
