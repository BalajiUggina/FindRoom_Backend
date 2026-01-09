from django.apps import AppConfig
import logging

logger=logging.getLogger('apps.rooms')

class RoomsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.rooms"
    label="rooms"

    def ready(self):
        logger.info("rooms app loaded successfully")