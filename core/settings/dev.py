from core.settings.base import *
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "asha_lab",
        "USER": "root",
        "PASSWORD": "password",
    }
}