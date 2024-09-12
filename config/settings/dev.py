import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = True

ALLOWED_HOSTS: list[str] = ["localhost", "127.0.0.1", "0.0.0.0"]

ROOT_URLCONF = "config.urls.development_urls"
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_NAME"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    }
}
