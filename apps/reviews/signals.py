from django.dispatch import receiver
from django.db.models import Avg
from django.db.models.signals import post_save

from .models import Rating


@receiver(post_save, sender=Rating)
def update_model_average_rating(sender, instance, **kwargs):
    model = instance.content_object
    ratings = Rating.objects.filter(content_type=instance.content_type, object_id=instance.object_id)
    average_rating = ratings.aggregate(Avg('rating_value'))['rating_value__avg']
    model.average_rating = average_rating
    model.save()
