from django.contrib.auth import get_user_model
from django.db import models

from .consts import ACCOUNT_TYPE, BANK_CODE

User = get_user_model()


class Accounts(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    bank_code = models.CharField(max_length=10, choices=BANK_CODE)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE)
    balance = models.DecimalField(max_digits=14, decimal_places=2, default=0)

    def __str__(self) -> str:
        return f"{self.bank_code} - {self.account_number}"
