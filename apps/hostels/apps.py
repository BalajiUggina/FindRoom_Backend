from django.apps import AppConfig
import logging

logger=logging.getLogger('apps.hostels')

class HostelsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.hostels"
    label="hostels"

    def ready(self):
        logger.info("hostels app loaded successfully")

