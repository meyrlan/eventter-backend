"""
Django production settings for eventter project.
"""


import os
import firebase_admin
import requests
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *  # noqa
from .base import env


# Sentry logging
def before_send(event, hint):
    # TODO: Enable this error again, once ELB check is fixed
    if "logger" in event and event["logger"] == "django.security.DisallowedHost":
        return
    return event


DEBUG = True
SECRET_KEY = "whatever"

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True  # TODO: Disable after front is done
CORS_URLS_REGEX = r"^/(website-api/logistics|api/tilda)/.*$"

DATABASES = {
    "default": {
        "ENGINE": env("SQL_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": env("SQL_DATABASE", default=str(ROOT_DIR / "db.sqlite3")),
        "USER": env("SQL_USER", default="postgres"),
        "PASSWORD": env("SQL_PASSWORD", default=""),
        "HOST": env("SQL_HOST", default="localhost"),
        "PORT": env("SQL_PORT", default="5432"),
    }
}


if 'DATABASE_URL' in os.environ:
    import dj_database_url
    DATABASES = {'default': dj_database_url.config()}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [
                (
                    env("REDIS_HOST", default="localhost"),
                    env.int("REDIS_PORT", default="6379"),
                )
            ],
        },
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
        "UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
