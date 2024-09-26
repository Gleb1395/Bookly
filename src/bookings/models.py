from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Booking(models.Model):
    """
    Model for hotel booking with fields for customer,
    hotel, room, arrival and departure dates, price and booking status.
    """

    ACTIVE = 1
    INACTIVE = 0

    BOOKING_STATUS_CHOICES = [
        (ACTIVE, _("Active")),
        (INACTIVE, _("Inactive")),
    ]

    client = models.ForeignKey(to="accounts.Client", on_delete=models.CASCADE, related_name="client")
    # hotel = ...
    # room = ...
    arrival_date = models.DateTimeField(_("arrival_date"), null=False, blank=False)
    departure_date = models.DateTimeField(_("departure_date"), null=False, blank=False)
    total_price = models.FloatField(
        _("Total price"),
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0.0),
        ],
    )
    booking_status = models.IntegerField(
        _("Booking status"),
        choices=BOOKING_STATUS_CHOICES,
        default=INACTIVE,
        blank=True,
        null=True,
    )
