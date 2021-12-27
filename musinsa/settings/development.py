from .base import *

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

SECRET_KEY = get_env_value("SECRET_KEY")

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
