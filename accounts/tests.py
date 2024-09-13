from django.test import TestCase
from .models import Account
from users.models import User

class AccountModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@example.com', name='Test User')

    def test_create_account(self):
        # Given
        account_data = {
            'user': self.user,
            'account_number': '1234567890',
            'bank_code': 'kakao_bank',
            'account_type': 'Savings',
            'balance': 1000
        }

        # When
        account = Account.objects.create(**account_data)

        # Then
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(account.user, self.user)
        self.assertEqual(account.account_number, '1234567890')
        self.assertEqual(account.bank_code, 'kakao_bank')
        self.assertEqual(account.account_type, 'Savings')
        self.assertEqual(account.balance, 1000)

    def test_account_str_method(self):
        # Given
        account = Account.objects.create(
            user=self.user,
            account_number='1234567890',
            bank_code='kakao_bank'
        )

        # When
        account_str = str(account)

        # Then
        self.assertEqual(account_str, 'Account: 1234567890 (ABC)')