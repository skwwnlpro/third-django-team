from django.db import models

from accounts.models import Accounts


class TransactionHistorys(models.Model):
    class TransactionTypeChoices(models.TextChoices):
        CASH = "cash", "Cash"
        TRANSFER = "transfer", "Transfer"
        AUTO_TRANSFER = "auto_transfer", "Auto Transfer"
        CARD_PAYMENT = "card_payment", "Card Payment"

    class DepositWithdrawalTypeChoices(models.TextChoices):
        DEPOSIT = "deposit", "Deposit"
        WITHDRAWAL = "withdrawal", "Withdrawal"

    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    transaction_amount = models.DecimalField(max_digits=14, decimal_places=2)
    transaction_type = models.CharField(max_length=15, choices=TransactionTypeChoices.choices)
    balance_after_transaction = models.DecimalField(max_digits=14, decimal_places=2)
    deposit_withdrawal_type = models.CharField(max_length=15, choices=DepositWithdrawalTypeChoices.choices)
    transaction_description = models.CharField(max_length=255)
    transaction_date = models.DateField(auto_now_add=True)
    transaction_time = models.TimeField(auto_now_add=True)
