from typing import Any, Dict
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str, **extra_fields: Dict[str, Any]) -> "Users":
        if not email:
            raise ValueError("Email 주소를 필수로 입력하세요.")
        # if Users.objects.filter(email=email).exists():
        #     raise ValidationError("해당 Email은 이미 존재합니다.")
        if password is None:
            raise ValueError("Password를 필수로 입력하세요.")
        if not (extra_fields.get("phone_number") and extra_fields.get("nickname")):
            raise ValueError("Phone번호와 Nickname은 필수로 입력하세요.")

        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)  # hash + salt
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, **extra_fields: Dict[str, Any]) -> "Users":
        if not (extra_fields.get("phone_number") and extra_fields.get("nickname")):
            raise ValueError("Phone번호와 Nickname은 필수로 입력하세요.")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_admin", True)
        user = self.create_user(email, password=password, **extra_fields)
        user.save(using=self._db)
        return user
