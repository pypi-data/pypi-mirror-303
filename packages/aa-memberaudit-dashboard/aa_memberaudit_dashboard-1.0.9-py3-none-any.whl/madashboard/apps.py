"""App Configuration"""

# Django
from django.apps import AppConfig

from madashboard import __version__


class MADashbaordConfig(AppConfig):
    """App Config"""

    default_auto_field = "django.db.models.AutoField"
    name = "madashboard"
    label = "madashboard"
    verbose_name = f"MemberAudit Dashboard v{__version__}"
