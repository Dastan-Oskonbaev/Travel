from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CultureConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.culture'
    verbose_name = _('Culture')
    verbose_name_plural = _('Cultures')
