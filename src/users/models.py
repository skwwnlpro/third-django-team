from typing import Any, Dict

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from common.models import BaseModel


class UserManager(BaseUserManager["Users"]):
    def create_user(self, email: str, password: str, **extra_fields: Dict[str, Any]) -> "Users":
        if not email:
            raise ValueError("Email 주소를 필수로 입력하세요.")
        if password is None:
            raise ValueError("Password를 필수로 입력하세요.")
        if not (extra_fields.get("phone_number") and extra_fields.get("nickname")):
            raise ValueError("Phone번호와 Nickname은 필수로 입력하세요.")

        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)  # hash + salt
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email: str, password: str, **extra_fields: Dict[str, Any]
    ) -> "Users":
        if not (extra_fields.get("phone_number") and extra_fields.get("nickname")):
            raise ValueError("Phone번호와 Nickname은 필수로 입력하세요.")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_admin", True)
        user = self.create_user(email, password=password, **extra_fields)
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, unique=True)
    last_login = models.DateTimeField(auto_now=True, null=True)

    # PermissionMixin: 권한 관리
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD: str = "email"
    # Email 이외에 사용자 생성에서 필수 필드
    REQUIRED_FIELDS: list[str] = ["nickname"]

    objects = UserManager()  # 유저를 생성 및 관리 (유저를 구분해서 관리하기 위해 - 관리자계정, 일반계정)

    def __str__(self) -> str:
        return f"email: {self.email}, nickname: {self.nickname}"
