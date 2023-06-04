from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PixelflowThemeConfig(AppConfig):
    name = "pixelflow_theme"
    verbose_name = _("Admin")
    default_auto_field = "django.db.models.AutoField"
