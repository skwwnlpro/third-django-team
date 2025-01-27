from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from typing import Any, Dict
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    # 이 옵션은 해당 필드가 쓰기 전용임을 나타냅니다.
    # 데이터 생성 또는 업데이트 시에만 사용되고, 직렬화된 출력에는 포함되지 않습니다.
    # 비밀번호와 같은 민감한 정보를 API 응답에 노출시키지 않기 위해 사용됩니다.
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["email", "password", "password2", "nickname", "name", "phone_number"]

    def validate(self, arr):
        if arr["password"] != arr["password2"]:
            raise serializers.ValidationError({"password": "Password didn't match."})
        return arr

    # User 생성
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            nickname=validated_data["nickname"],
            phone_number=validated_data["phone_number"],
        )

        # Email 인증 후
        user.is_active = False
        user.save()

        return user


class LoginSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, arr: Dict[str, Any]) -> Dict[str, Any]:
        email = arr.get("email")
        password = arr.get("password")

        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError("Email or password is incorrect")

        arr["user"] = user
        return arr


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name"]
