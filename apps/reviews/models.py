from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model


User = get_user_model()


class Review(models.Model):
    text = models.TextField(
        _('Text'),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name=_('Author'),
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name=_('Content type'),
    )
    object_id = models.PositiveIntegerField(
        _('Object id'),
    )
    content_object = GenericForeignKey(
        'content_type',
        'object_id',
    )

    def __str__(self):
        return f"Review by {self.author} on {self.content_object}"

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')


class Rating(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ratings',
        verbose_name=_('User'),
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name='ratings',
        verbose_name=_('Content type'),
    )
    object_id = models.PositiveIntegerField(
        _('Object id'),
    )
    content_object = GenericForeignKey(
        'content_type',
        'object_id',
    )
    rating_value = models.PositiveIntegerField(
        _('Rating value'),
        choices=[
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        ],
        default=5,
    )

    def __str__(self):
        return f'Rating {self.rating_value} by {self.user} on {self.content_object}'

    class Meta:
        verbose_name = _('Rating')
        verbose_name_plural = _('Ratings')
        unique_together = ['user', 'content_type', 'object_id']


class RestaurantRating(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='restaurant_rating',
        verbose_name=_('User'),
    )
    restaurant = models.ForeignKey(
        'places.Restaurants',
        on_delete=models.CASCADE,
        related_name='rating',
        verbose_name=_('Restaurant')
    )
    rating = models.DecimalField(
        _('Rating'),
        max_digits=3,
        decimal_places=2,
        default=0,
        null=True,
        blank=True,
    )
    nutrition = models.DecimalField(
        _('Nutrition'),
        max_digits=3,
        decimal_places=2,
        default=0,
    )
    service = models.DecimalField(
        _('Service'),
        max_digits=3,
        decimal_places=2,
        default=0,
    )
    price_quality = models.DecimalField(
        _('Price Quality'),
        max_digits=3,
        decimal_places=2,
        default=0,
    )
    atmosphere = models.DecimalField(
        _('Atmosphere'),
        max_digits=3,
        decimal_places=2,
        default=0,
    )

    def __str__(self):
        return f'Rating {self.rating} by {self.user} on {self.restaurant.name}'

    class Meta:
        verbose_name = _('Restaurant Rating')
        verbose_name_plural = _('Restaurants Rating')
