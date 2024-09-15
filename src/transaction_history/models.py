from django.db import models

from accounts.models import Accounts

from .consts import PAYMENT_TYPE, TRANSACTION_TYPE


class TransactionHistory(models.Model):
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    balance = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPE)
    payment_type = models.CharField(max_length=15, choices=PAYMENT_TYPE)
    transaction_description = models.CharField(max_length=255)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.account} - {self.get_transaction_type_display()} - {self.amount}"
