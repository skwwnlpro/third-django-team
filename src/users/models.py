from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from users.manager import UserManager
from common.models import BaseModel


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
    REQUIRED_FIELDS: list[str] = ["nickname", "name", "phone_number"]

    objects = UserManager()  # 유저를 생성 및 관리 (유저를 구분해서 관리하기 위해 - 관리자계정, 일반계정)

    def __str__(self) -> str:
        return f"email: {self.email}, nickname: {self.nickname}"
