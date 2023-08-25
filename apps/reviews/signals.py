from django.dispatch import receiver
from django.db.models import Avg
from django.db.models.signals import post_save

from .models import Rating, RestaurantRating


@receiver(post_save, sender=Rating)
def update_model_average_rating(sender, instance, **kwargs):
    model = instance.content_object
    ratings = Rating.objects.filter(content_type=instance.content_type, object_id=instance.object_id)
    average_rating = ratings.aggregate(Avg('rating_value'))['rating_value__avg']
    model.average_rating = average_rating
    model.save()


@receiver(post_save, sender=RestaurantRating)
def update_restaurant_average_rating(sender, instance, **kwargs):
    restaurant = instance.restaurant
    average_rating = RestaurantRating.objects.filter(
        restaurant=restaurant
    ).aggregate(Avg('rating'))['rating__avg']
    if average_rating is not None:
        restaurant.average_rating = average_rating
        restaurant.save()
