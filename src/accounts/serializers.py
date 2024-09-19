from django.db.models import QuerySet
from rest_framework import serializers
from .models import Accounts
from users.serializers import UserSerializer


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accounts
        fields = ["id", "account_type", "balance"]


class AccountCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accounts
        fields = ["bank_code", "account_type"]


class AccountListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    balance = serializers.SerializerMethodField()

    class Meta:
        model = Accounts
        fields = ["user", "account_number", "balance"]

    @staticmethod
    def get_optimized_queryset() -> QuerySet:
        return Accounts.objects.select_related("user").only("user", "account_number", "balance")

    def get_balance(self, instance) -> str:  # type: ignore
        return f"{int(instance.balance)}원"


class AccountRetrieveSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    balance = serializers.SerializerMethodField()

    class Meta:
        model = Accounts
        fields = ["user", "account_number", "balance"]

    @staticmethod
    def get_optimized_queryset() -> QuerySet:
        return Accounts.objects.select_related("user").only("user", "account_number", "balance")

    def get_balance(self, instance) -> str:  # type: ignore
        return f"{int(instance.balance)}원"


class AccountDestroySerializer(serializers.ModelSerializer):
    @staticmethod
    def get_optimized_queryset() -> QuerySet:
        return Accounts.objects.all()
