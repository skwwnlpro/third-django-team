from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import Accounts
from decimal import Decimal
from .consts import ACCOUNT_TYPE, BANK_CODE

User = get_user_model()


# Create your tests here.
class AccountModelTest(TestCase):
    # Given
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="qwe123",
            nickname="aabb",
            name="abc",
            phone_number="123123123",
        )
        self.account = Accounts.objects.create(
            user_id=self.user,  # 'user'를 'user_id'로 변경
            account_num="1234567890",
            bank_code="kb",
            account_type="savings",
            balance=Decimal("1000.00"),
        )
