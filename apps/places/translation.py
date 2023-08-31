from modeltranslation.translator import register, TranslationOptions

from .models import (
    Region,
    WhatToTry,
    Place, Hotels,
    Restaurants,
    EventsCategory,
    Events,
    Attractions,
)


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(WhatToTry)
class WhatToTryTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(Place)
class PlaceTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(Hotels)
class HotelsTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'address',)


@register(Restaurants)
class RestaurantsTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'specialized_menu', 'address',)


@register(EventsCategory)
class EventsCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Events)
class EventsTranslationOptions(TranslationOptions):
    fields = ('name', 'address',)


@register(Attractions)
class AttractionsTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
