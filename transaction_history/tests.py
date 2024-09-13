from django.test import TestCase
from .models import TransactionHistory
from users.models import User
from accounts.models import Account
from django.utils import timezone

class TransactionHistoryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@example.com', name='Test User')
        self.account = Account.objects.create(
            user=self.user,
            account_number='1234567890',
            bank_code='kakao_bank',
            balance=1000
        )

    def test_create_transaction_history(self):
        # Given
        transaction_data = {
            'account': self.account,
            'transaction_amount': 500,
            'transaction_balance': 1500,
            'account_history': 'Deposit',
            'transaction_type': 'Credit',
            'transaction_time': timezone.now()
        }

        # When
        transaction = TransactionHistory.objects.create(**transaction_data)

        # Then
        self.assertEqual(TransactionHistory.objects.count(), 1)
        self.assertEqual(transaction.account, self.account)
        self.assertEqual(transaction.transaction_amount, 500)
        self.assertEqual(transaction.transaction_balance, 1500)
        self.assertEqual(transaction.account_history, 'Deposit')
        self.assertEqual(transaction.transaction_type, 'Credit')
        self.assertIsNotNone(transaction.transaction_time)

    def test_transaction_history_str_method(self):
        # Given
        transaction = TransactionHistory.objects.create(
            account=self.account,
            transaction_amount=500,
            transaction_balance=1500,
            account_history='Deposit',
            transaction_type='Credit',
            transaction_time=timezone.now()
        )

        # When
        transaction_str = str(transaction)

        # Then
        expected_str = f'Transaction: {transaction.id} - Amount: 500 - Type: Credit'
        self.assertEqual(transaction_str, expected_str)