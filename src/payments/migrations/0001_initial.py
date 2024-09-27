# Generated by Django 4.2 on 2024-09-26 14:21

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bookings", "0003_alter_booking_client"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "data_of_payment",
                    models.DateField(
                        blank=True, null=True, verbose_name="data of payment"
                    ),
                ),
                (
                    "amount",
                    models.FloatField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0.0)],
                        verbose_name="amount",
                    ),
                ),
                (
                    "payment_method",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("CREDIT_CARD", "Credit Card"),
                            ("PAYPAL", "PayPal"),
                            ("BANK_TRANSFER", "Bank Transfer"),
                            ("CASH", "Cash"),
                        ],
                        max_length=20,
                        null=True,
                        verbose_name="payment method",
                    ),
                ),
                (
                    "payment_status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("PENDING", "Pending"),
                            ("COMPLETED", "Completed"),
                            ("FAILED", "Failed"),
                            ("CANCELLED", "Cancelled"),
                        ],
                        max_length=20,
                        null=True,
                        verbose_name="payment status",
                    ),
                ),
                (
                    "bookings",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookings",
                        to="bookings.booking",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payment",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
