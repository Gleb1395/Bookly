from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Payment(models.Model):
    """
    A model for storing payment information.
    """

    PAYMENT_METHOD_CHOICES = [
        ('CREDIT_CARD', _('Credit Card')),
        ('PAYPAL', _('PayPal')),
        ('BANK_TRANSFER', _('Bank Transfer')),
        ('CASH', _('Cash')),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('PENDING', _('Pending')),
        ('COMPLETED', _('Completed')),
        ('FAILED', _('Failed')),
        ('CANCELLED', _('Cancelled')),
    ]
    client = models.ForeignKey(to="accounts.Client", on_delete=models.CASCADE, related_name='payment', null=True)
    bookings = models.ForeignKey(to="bookings.Booking", on_delete=models.CASCADE, related_name='bookings', null=True)
    data_of_payment = models.DateField(_("data of payment"), blank=True, null=True)
    amount = models.FloatField(
        _("amount"),
        blank=True,
        null=True,
        validators=[MinValueValidator(0.0), ],
    )
    payment_method = models.CharField(
        _("payment method"),
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
        blank=True,
        null=True
    )
    payment_status = models.CharField(
        _("payment status"),
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        blank=True,
        null=True
    )
