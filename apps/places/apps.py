from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PlacesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.places'
    verbose_name = _('Place')
    verbose_name_plural = _('Places')
