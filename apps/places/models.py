from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation

from datetime import date

from phonenumber_field.modelfields import PhoneNumberField

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
    average_rating = models.DecimalField(
        _('Average Rating'),
        max_digits=3,
        decimal_places=2,
        default=0,
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
    bedrooms = models.PositiveIntegerField(
        _('Bedrooms')
    )
    bathrooms = models.PositiveIntegerField(
        _('Bathrooms')
    )
    car_parking = models.PositiveIntegerField(
        _('Car Parking')
    )
    pets = models.PositiveIntegerField(
        _('Pets')
    )
    price = models.CharField(
        _('Price'),
        max_length=100
    )
    kitchen = models.BooleanField(
        _('Kitchen'),
        default=False
    )
    conditioner = models.BooleanField(
        _('Conditioner'),
        default=False
    )
    washer = models.BooleanField(
        _('Washer'),
        default=False
    )
    tv_netflix = models.BooleanField(
        _('TV with Netflix'),
        default=False
    )
    wifi = models.BooleanField(
        _('Free Wi-Fi'),
        default=False
    )
    balcony = models.BooleanField(
        _('Balcony or Patio'),
        default=False
    )
    garden = models.BooleanField(
        _('Green space or gardens'),
        default=False
    )
    car_rent = models.BooleanField(
        _('Car rental services'),
        default=False
    )
    hairdryer = models.BooleanField(
        _('Hairdryers'),
        default=False
    )
    iron_board = models.BooleanField(
        _('Iron and ironing board'),
        default=False
    )
    pool = models.BooleanField(
        _('Swimming pool'),
        default=False
    )
    gym = models.BooleanField(
        _('Fitness center or gym'),
        default=False
    )
    game_room = models.BooleanField(
        _('Game room'),
        default=False
    )
    address = models.CharField(
        _('Address'),
        max_length=100,
        null=True,
        blank=True
    )
    phone_number = PhoneNumberField(
        _('Phone Number')
    )
    reviews = GenericRelation(
        Review,
        verbose_name=_('Reviews'),
    )
    average_rating = models.DecimalField(
        _('Average Rating'),
        max_digits=3,
        decimal_places=2,
        default=0,
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
        _('Price Range'),
        max_length=100
    )
    specialized_menu = models.CharField(
        _('Specialized menu'),
        max_length=100
    )
    meal_time = models.CharField(
        _('Meal Time'),
        max_length=100
    )
    website = models.URLField(
        _('Website')
    )
    address = models.CharField(
        _('Address'),
        max_length=100
    )
    email = models.EmailField(
        _('Email')
    )
    phone_number = PhoneNumberField(
        _('Phone Number')
    )
    reviews = GenericRelation(
        Review,
        verbose_name=_('Reviews'),
    )
    average_rating = models.DecimalField(
        _('Average Rating'),
        max_digits=3,
        decimal_places=2,
        default=0,
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


class EventsCategory(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Events Category')
        verbose_name_plural = _('Events Categories')


class Events(models.Model):
    category = models.ForeignKey(
        EventsCategory,
        on_delete=models.CASCADE,
        related_name='event',
        verbose_name=_('Events Category'),
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='events',
        verbose_name=_('Place')
    )
    name = models.CharField(
        _('Name'),
        max_length=100
    )
    date = models.DateField(
        _('Date'),
        default=date.today,
    )
    time = models.CharField(
        _('Time'),
        max_length=20
    )
    address = models.CharField(
        _('Address'),
        max_length=100
    )
    poster = models.ImageField(
        _('Poster'),
        upload_to=f'events {name}',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')


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
    contacts = PhoneNumberField(
        _('Contacts'),
        null=True,
        blank=True
    )
    reviews = GenericRelation(
        Review,
        verbose_name=_('Reviews'),
    )
    average_rating = models.DecimalField(
        _('Average Rating'),
        max_digits=3,
        decimal_places=2,
        default=0,
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
