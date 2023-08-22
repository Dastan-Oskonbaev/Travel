from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation

from apps.reviews.models import Review


class Region(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100
    )
    photo = models.ImageField(
        _('Photo'),
        upload_to=f'regions {name}',
        blank=True,
        null=True
    )
    description = models.TextField(
        _('Description'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')


class WhatToTry(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100
    )
    description = models.TextField(
        _('Description'),
    )
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name='what_to_try',
        verbose_name=_('Region')
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('What to try')
        verbose_name_plural = _('What to try')


class WhatToTryImage(models.Model):
    what_to_try = models.ForeignKey(
        WhatToTry,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('What to try')
    )
    image = models.ImageField(
        _('Image'),
        upload_to=f'what_to_try {what_to_try.name}',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.what_to_try.name

    class Meta:
        verbose_name = _('What to try image')
        verbose_name_plural = _('What to try images')


class Place(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100
    )
    description = models.TextField(
        _('Description'),
    )
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name='places',
        verbose_name=_('Region')
    )
    reviews = GenericRelation(
        Review,
        verbose_name=_('Reviews'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Place')
        verbose_name_plural = _('Places')


class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('Place')
    )
    image = models.ImageField(
        _('Image'),
        upload_to=f'place {place.name}',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.place.name

    class Meta:
        verbose_name = _('Place image')
        verbose_name_plural = _('Place images')


class Hotels(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100
    )
    description = models.TextField(
        _('Description'),
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='hotels',
        verbose_name=_('Place')
    )
    reviews = GenericRelation(
        Review,
        verbose_name=_('Reviews'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Hotel')
        verbose_name_plural = _('Hotels')


class HotelsImage(models.Model):
    hotels = models.ForeignKey(
        Hotels,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('Hotel')
    )
    image = models.ImageField(
        _('Image'),
        upload_to=f'hotels {hotels.name}',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.hotels.name

    class Meta:
        verbose_name = _('Hotel image')
        verbose_name_plural = _('Hotel images')


class Restaurants(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100
    )
    description = models.TextField(
        _('Description'),
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='restaurants',
        verbose_name=_('Place')
    )
    price_range = models.CharField(
        max_length=100
    )
    specialized_menu = models.CharField(
        max_length=100
    )
    reviews = GenericRelation(
        Review,
        verbose_name=_('Reviews'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Restaurant')
        verbose_name_plural = _('Restaurants')


class RestaurantsImage(models.Model):
    restaurants = models.ForeignKey(
        Restaurants,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('Restaurant')
    )
    image = models.ImageField(
        _('Image'),
        upload_to=f'restaurants {restaurants.name}',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.restaurants.name

    class Meta:
        verbose_name = _('Restaurant image')
        verbose_name_plural = _('Restaurant images')


class Events(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100
    )
    description = models.TextField(
        _('Description'),
    )
    date = models.DateTimeField(
        _('Date'),
        auto_now_add=True,
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='events',
        verbose_name=_('Place')
    )
    address = models.CharField(
        _('Address'),
        max_length=100
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')


class EventsImage(models.Model):
    events = models.ForeignKey(
        Events,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('Event')
    )
    image = models.ImageField(
        _('Image'),
        upload_to=f'events {events.name}',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.events.name

    class Meta:
        verbose_name = _('Event image')
        verbose_name_plural = _('Event images')


class Attractions(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100
    )
    description = models.TextField(
        _('Description'),
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='attractions',
        verbose_name=_('Place')
    )
    reviews = GenericRelation(
        Review,
        verbose_name=_('Reviews'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Attraction')
        verbose_name_plural = _('Attractions')


class AttractionsImage(models.Model):
    attractions = models.ForeignKey(
        Attractions,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('Attraction')
    )
    image = models.ImageField(
        _('Image'),
        upload_to=f'attractions {attractions.name}',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.attractions.name

    class Meta:
        verbose_name = _('Attraction image')
        verbose_name_plural = _('Attraction images')
