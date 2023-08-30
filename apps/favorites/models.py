from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import CustomUser
from apps.places.models import Place, Hotels, Restaurants, Attractions


class Favorite(models.Model):
    customer = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name=_('User'),
    )

    def __str__(self):
        return f"Favorite for {self.customer.username}"

    class Meta:
        verbose_name = _('Favorite')
        verbose_name_plural = _('Favorites')


class FavoritePlaces(models.Model):
    favorite = models.ForeignKey(
        Favorite,
        on_delete=models.CASCADE,
        related_name='favorite_places',
        verbose_name=_('Favorite'),
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name=_('Place'),
    )

    def __str__(self):
        return f"{self.place.name} in {self.favorite}"

    class Meta:
        verbose_name = _('Favorite Place')
        verbose_name_plural = _('Favorite Places')


class FavoriteHotels(models.Model):
    favorite = models.ForeignKey(
        Favorite,
        on_delete=models.CASCADE,
        related_name='favorite_hotels',
        verbose_name=_('Favorite'),
    )
    hotel = models.ForeignKey(
        Hotels,
        on_delete=models.CASCADE,
        verbose_name=_('Hotel'),
    )

    def __str__(self):
        return f"{self.hotel.name} in {self.favorite}"

    class Meta:
        verbose_name = _('Favorite Hotel')
        verbose_name_plural = _('Favorite Hotels')


class FavoriteRestaurants(models.Model):
    favorite = models.ForeignKey(
        Favorite,
        on_delete=models.CASCADE,
        related_name='favorite_restaurants',
        verbose_name=_('Favorite'),
    )
    restaurant = models.ForeignKey(
        Restaurants,
        on_delete=models.CASCADE,
        verbose_name=_('Restaurant'),
    )

    def __str__(self):
        return f"{self.restaurant.name} in {self.favorite}"

    class Meta:
        verbose_name = _('Favorite Restaurant')
        verbose_name_plural = _('Favorite Restaurants')


class FavoriteAttractions(models.Model):
    favorite = models.ForeignKey(
        Favorite,
        on_delete=models.CASCADE,
        related_name='favorite_attractions',
        verbose_name=_('Favorite'),
    )
    attraction = models.ForeignKey(
        Attractions,
        on_delete=models.CASCADE,
        verbose_name=_('Attraction'),
    )

    def __str__(self):
        return f"{self.attraction.name} in {self.favorite}"

    class Meta:
        verbose_name = _('Favorite Attraction')
        verbose_name_plural = _('Favorite Attractions')
