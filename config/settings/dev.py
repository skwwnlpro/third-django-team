import os

DEBUG = True

ALLOWED_HOSTS: list[str] = ["localhost", "127.0.0.1"]

ROOT_URLCONF = "config.urls.development_urls"
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": "localhost",
        "PORT": "5432",
    }
}
