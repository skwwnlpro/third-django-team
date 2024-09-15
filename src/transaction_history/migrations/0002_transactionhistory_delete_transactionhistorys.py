# Generated by Django 5.1.1 on 2024-09-15 14:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_accounts_account_type_alter_accounts_bank_code"),
        ("transaction_history", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TransactionHistory",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("amount", models.DecimalField(decimal_places=2, max_digits=14)),
                ("balance", models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                (
                    "transaction_type",
                    models.CharField(choices=[("deposit", "Deposit"), ("withdrawal", "Withdrawal")], max_length=15),
                ),
                (
                    "payment_type",
                    models.CharField(
                        choices=[
                            ("cash", "Cash"),
                            ("transfer", "Transfer"),
                            ("auto_transfer", "Auto Transfer"),
                            ("card_payment", "Card Payment"),
                        ],
                        max_length=15,
                    ),
                ),
                ("transaction_description", models.CharField(max_length=255)),
                ("transaction_date", models.DateTimeField(auto_now_add=True)),
                ("account", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="accounts.accounts")),
            ],
        ),
        migrations.DeleteModel(
            name="TransactionHistorys",
        ),
    ]