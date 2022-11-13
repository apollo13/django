DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "postgres",
        "NAME": "django",
    },
    "other": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "postgres",
        "NAME": "django2",
    },
}

SECRET_KEY = "django_tests_secret_key"

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

USE_TZ = False
