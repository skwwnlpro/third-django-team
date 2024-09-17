import os, json
from pathlib import Path

from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

with open(BASE_DIR / "secret.json") as f:
    config_secret_str = f.read()

SECRET = json.loads(config_secret_str)

# No Debug Mode in Production
DEBUG = True

ALLOWED_HOSTS: list[str | None | int] = ["localhost", "127.0.0.1", "0.0.0.0"]

SECRET_KEY = SECRET["DJANGO_SECRET_KEY"]

ROOT_URLCONF = "config.urls"


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


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # own apps
    "users",
    "accounts",
    "transaction_history",
    "rest_framework",
    "rest_framework_simplejwt",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Auth
AUTH_USER_MODEL = "users.Users"

# 이메일을 보내기 위한 백엔드 설정
# from django.core.mail.backends.smtp import EmailBackend
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# SMTP 서버 설정
EMAIL_HOST = "smtp.gmail.com"  # SMTP 서버 주소
EMAIL_USE_TLS = True  # TLS 사용 여부
EMAIL_PORT = 587  # TLS 포트 번호
EMAIL_HOST_USER = SECRET["email"]["user"]
EMAIL_HOST_PASSWORD = SECRET["email"]["password"]


# DRF JWT 인증 설정
SIMPLE_JWT = {
    # 액세스 토큰의 유효 기간을 5분으로 설정합니다.
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    # 리프레시 토큰의 유효 기간을 1일로 설정합니다.
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    # 리프레시 토큰을 갱신할 때마다 새 토큰을 생성하지 않도록 설정합니다.
    "ROTATE_REFRESH_TOKENS": False,
    # 토큰을 갱신한 후 이전 토큰을 블랙리스트에 추가합니다.
    "BLACKLIST_AFTER_ROTATION": True,
    # JWT에 사용할 서명 알고리즘으로 HS256을 사용합니다.
    "ALGORITHM": "HS256",
    # JWT를 서명하는 데 사용할 키로 Django의 SECRET_KEY를 사용합니다.
    "SIGNING_KEY": SECRET_KEY,
    # JWT 검증에 사용할 키입니다. HS256 알고리즘에서는 None으로 설정됩니다.
    "VERIFYING_KEY": None,
    # 인증 헤더의 타입으로 'Bearer'를 사용합니다.
    # Authorization: Bearer <token>
    "AUTH_HEADER_TYPES": ("Bearer",),
    # 토큰에 포함될 사용자 식별자 필드로 'id'를 사용합니다.
    "USER_ID_FIELD": "id",
    # 토큰 클레임에서 사용자 식별자에 해당하는 키로 'user_id'를 사용합니다.
    "USER_ID_CLAIM": "user_id",
    # 사용할 토큰 클래스로 AccessToken을 사용합니다.
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}
