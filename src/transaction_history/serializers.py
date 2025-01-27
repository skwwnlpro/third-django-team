from rest_framework import serializers
from accounts.serializers import AccountSerializer
from transaction_history.models import TransactionHistory


class TransactionHistoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransactionHistory
        fields = [
            "account",
            "transaction_amount",
            "transaction_type",
            "payment_method",
            "transaction_description",
        ]


class TransactionHistorySerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = TransactionHistory
        fields = [
            "account",
            "transaction_amount",
            "transaction_balance",
            "transaction_type",
            "payment_method",
            "transaction_description",
        ]
