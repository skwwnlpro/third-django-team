from django.contrib.auth import get_user_model
from common.models import BaseModel
from django.db import models
from decimal import Decimal

from .consts import ACCOUNT_TYPE, BANK_CODE


class Accounts(BaseModel):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    account_number = models.CharField(max_length=50, unique=True)
    bank_code = models.CharField(max_length=50, choices=BANK_CODE)
    account_type = models.CharField(max_length=50, choices=ACCOUNT_TYPE)
    balance = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal("0.00"))

    def __str__(self) -> str:
        return f"{self.bank_code} - {self.account_number}"
