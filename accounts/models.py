from django.db import models
from users.models import User

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.IntegerField()
    bank_code = models.CharField(max_length=20)
    account_type = models.CharField(max_length=10)
    balance = models.IntegerField()

    def __str__(self):
        return f"Account: {self.account_number} ({self.bank_code})"