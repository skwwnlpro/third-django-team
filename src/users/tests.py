from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTest(TestCase):
    def setUp(self):
        self.user_data = {"email": "test@example.com", "password": "test1234"}

    def test_create_user(self):
        # When : 입력 받은 데이터를 바탕으로 유저 모델을 생성하면
        user = User.objects.create_user(**self.user_data)

        # Then : 성공적으로 생성된 유저모델은 이메일, 닉네임, 비밀번호가 입력받은 데이터와 일치해야 한다.
        self.assertEqual(user.email, self.user_data["email"])
        self.assertTrue(user.check_password(self.user_data["password"]))
