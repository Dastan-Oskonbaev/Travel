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
    rating = models.PositiveIntegerField(
        _('Rating'),
        default=0,
        null=True,
        blank=True,
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
