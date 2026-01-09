import logging
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from apps.common.exceptions import ValidationError
from apps.users.models import User

logger=logging.getLogger('apps.users')


def register_user(*,data):
    user=User(**data)
    user.set_password(data["password"])
    user.save()

    logger.info("New user registered:%s",user.email)
    return user


def login_user(*,email,password):
    user=authenticate(email=email,password=password)
    if not user:
        logger.warning("Login failed attempt for email:%s",user)
        raise ValidationError("Invalid Credentials")
    
    refresh=RefreshToken.for_user(user)
    logger.info("User logged in:%s",user.email)
    return {
        "access":str(refresh.access_token),
        "refresh":str(refresh),
    }


def update_user_role(*,user,role):
    user.role=role
    user.save()
    logger.info("User %s updated role to %s",user.id,role)
    return user