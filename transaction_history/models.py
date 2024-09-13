from django.db import models
from accounts.models import Account

class TransactionHistory(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_amount = models.IntegerField()
    transaction_balance = models.IntegerField()
    account_history = models.CharField(max_length=30, null=True)
    transaction_type = models.CharField(max_length=20)
    transaction_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction: {self.id} - Amount: {self.transaction_amount} - Type: {self.transaction_type}"

class AccountsTransactionHistory(models.Model):
    at_id = models.IntegerField(primary_key=True)
    transaction_id = models.ForeignKey(TransactionHistory, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = 'accounts_transaction_history'