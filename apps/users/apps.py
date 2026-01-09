from django.apps import AppConfig
import logging

logger=logging.getLogger("apps.users")

class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.users"
    label = "users"


    def ready(self):
        logger.info("users app loaded successfully")