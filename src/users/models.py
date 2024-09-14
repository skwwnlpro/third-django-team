from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from typing import Union


class UserManager(BaseUserManager["Users"]):
    def create_user(self, email: str, password: Union[str, None] = None) -> "Users":
        """
        Creates and saves a User with the given email, password.s
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: Union[str, None] = None) -> "Users":
        """
        Creates and saves a superuser with the given email, password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=20, unique=True, blank=False)
    password = models.CharField(max_length=100, blank=False)
    nickname = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=15, blank=False)
    phone_number = models.IntegerField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)

    # PermissionMixin: 권한 관리
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()  # 유저를 생성 및 관리 (유저를 구분해서 관리하기 위해 - 관리자계정, 일반계정)

    def __str__(self) -> str:
        return f"email: {self.email}, nickname: {self.nickname}"
