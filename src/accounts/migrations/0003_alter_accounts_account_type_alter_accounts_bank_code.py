# Generated by Django 5.1.1 on 2024-09-15 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accounts",
            name="account_type",
            field=models.CharField(
                choices=[
                    ("savings", "Savings Account"),
                    ("checking", "Checking Account"),
                    ("Loan", "Loan Account"),
                    ("overdraft", "Overdraft Account"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="accounts",
            name="bank_code",
            field=models.CharField(
                choices=[
                    ("kakao", "Kakao Bank"),
                    ("kb", "KB Kookmin Bank"),
                    ("nh", "NH NongHyup Bank"),
                    ("ibk", "IBK Industrial Bank of Korea"),
                    ("sh", "ShinHan Bank"),
                ],
                max_length=10,
            ),
        ),
    ]
