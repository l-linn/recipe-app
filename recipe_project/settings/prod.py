import environ
import os

from .base import *

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(str(BASE_DIR / ".env_prod"))

SECRET_KEY = env.str("SECRET_KEY")
# DEBUG = env.bool("DEBUG")
DEBUG = True

ALLOWED_HOSTS = [".herokuapp.com", "localhost", "127.0.0.1", "0.0.0.0"]
CSRF_TRUSTED_ORIGINS = [
    "https://localhost",
    "https://127.0.0.1",
    "https://0.0.0.0",
    "https://pacific-tor-80142-ffb5d961053d.herokuapp.com",
]

MIDDLEWARE = ["whitenoise.middleware.WhiteNoiseMiddleware"] + MIDDLEWARE

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "dmmf1k2lve5ea",  # database name
        "USER": "u2qtl6qvrdscu4",  # database user
        "PASSWORD": "p9929f8f28da996d73df20eefd9c5dafff7ba67ba6706e399bf87184d12d5fc72",  # database password
        "HOST": "c3nv2ev86aje4j.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com",
        "PORT": "5432",
    }
}

# Heroku: Update database configuration from $DATABASE_URL.
# import dj_database_url

# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES["default"].update(db_from_env)

CORS_ORIGIN_ALLOW_ALL = True

import django_on_heroku

django_on_heroku.settings(locals())
del DATABASES["default"]["OPTIONS"]["sslmode"]
