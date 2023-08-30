from django.db import models
from django.utils.translation import gettext_lazy as _


class CultureCategory(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100
    )
    description = models.TextField(
        _('Description'),
    )
    image = models.ImageField(
        _('Image'),
        upload_to=f'culture_category/{name}',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Culture Category')
        verbose_name_plural = _('Culture Categories')


class Culture(models.Model):
    category = models.ForeignKey(
        CultureCategory,
        on_delete=models.CASCADE,
        related_name='cultures',
        verbose_name=_('Category')
    )
    name = models.CharField(
        _('Name'),
        max_length=100
    )
    description = models.TextField(
        _('Description'),
    )
    image = models.ImageField(
        _('Image'),
        upload_to=f'culture/{name}',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Culture')
        verbose_name_plural = _('Cultures')
