from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError  # 데이터 유효성 검사 과정에서 발생하는 예외(exception)

# 현재 프로젝트에서 사용 중인 User 모델 클래스를 반환합니다.
# 기본적으로 Django의 내장 User 모델(django.contrib.auth.models.User)을 반환합니다.
# 만약 프로젝트에서 커스텀 User 모델을 정의하고 settings.AUTH_USER_MODEL에 지정했다면, 해당 커스텀 모델을 반환합니다.
User = get_user_model()


class UserModelTest(TestCase):
    # Given
    def setUp(self):
        self.user_data = {
            "email": "test@example.com",
            "password": "test1234",
        }

    def test_create_user(self):
        # When : 입력 받은 데이터를 바탕으로 유저 모델을 생성하면
        user = User.objects.create_user(**self.user_data)

        # Then : 성공적으로 생성된 유저모델은 이메일, 닉네임, 비밀번호가 입력받은 데이터와 일치해야 한다.
        self.assertEqual(user.email, self.user_data["email"])
        self.assertTrue(user.check_password(self.user_data["password"]))

    # def test_create_superuser(self):
    #     admin_user = User.objects.create_superuser(
    #         email="admin@example.com", password="adminpass123", nickname="adminnick"
    #     )
    #     self.assertEqual(admin_user.email, "admin@example.com")
    #     self.assertEqual(admin_user.nickname, "adminnick")
    #     self.assertTrue(admin_user.is_active)
    #     self.assertTrue(admin_user.is_staff)
    #     self.assertTrue(admin_user.is_admin)

    # def test_email_unique(self):
    #     User.objects.create_user(
    #         email="unique@example.com",
    #         password="testpass123",
    #         nickname="uniquenick",
    #         name="Unique User",
    #         phone_number="1111111111",
    #     )
    #     with self.assertRaises(ValidationError):
    #         user2 = User(
    #             email="unique@example.com",
    #             password="testpass123",
    #             nickname="uniquenick2",
    #             name="Unique User 2",
    #             phone_number="2222222222",
    #         )
    #         user2.full_clean()

    # def test_nickname_required(self):
    #     with self.assertRaises(ValueError):
    #         User.objects.create_user(
    #             email="test@example.com",
    #             password="testpass123",
    #             nickname="",
    #             name="Test User",
    #             phone_number="1234567890",
    #         )

    # def test_str_representation(self):
    #     user = User.objects.create_user(
    #         email="test@example.com",
    #         password="testpass123",
    #         nickname="testnick",
    #         name="Test User",
    #         phone_number="1234567890",
    #     )
    #     self.assertEqual(str(user), "email: test@example.com, nickname: testnick")

    # def test_phone_number_unique(self):
    #     User.objects.create_user(
    #         email="test1@example.com",
    #         password="testpass123",
    #         nickname="testnick1",
    #         name="Test User 1",
    #         phone_number="1234567890",
    #     )
    #     with self.assertRaises(ValidationError):
    #         user2 = User(
    #             email="test2@example.com",
    #             password="testpass123",
    #             nickname="testnick2",
    #             name="Test User 2",
    #             phone_number="1234567890",
    #         )
    #         user2.full_clean()
