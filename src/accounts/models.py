import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from accounts.manager import ClientManager


class Client(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model for the system, inheriting from AbstractBaseUser and PermissionsMixin.

    This model represents a client in the system and extends the default user model with additional fields

    Key features:
    - Uses email as the unique identifier for authentication.
    - Tracks client status (active, inactive, blocked).
    - UUID is used as the primary key for better scalability.
    """

    ACTIVE = 1
    INACTIVE = 0
    BLOCKED = -1

    CLIENT_STATUS_CHOICES = [
        (ACTIVE, _("Active")),
        (INACTIVE, _("Inactive")),
        (BLOCKED, _("Blocked")),
    ]

    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    first_name = models.CharField(_("name"), max_length=120, blank=True, null=True)
    last_name = models.CharField(_("surname"), max_length=120, blank=True, null=True)
    email = models.EmailField(
        _("email address"),
        unique=True,
        blank=False,
        null=False,
        max_length=254,
        error_messages={"unique": _("A user with that email already exists.")},
    )
    phone_number = PhoneNumberField(_("phone number"), blank=True, null=True)
    date_of_birth = models.DateField(_("date of birth"), blank=True, null=True)
    country = models.CharField(_("country"), max_length=150, blank=True, null=True)
    city = models.CharField(_("city"), max_length=150, blank=True, null=True)
    registration_date = models.DateField(_("registration date"), blank=True, null=True)
    client_status = models.IntegerField(
        _("client status"),
        choices=CLIENT_STATUS_CHOICES,
        default=ACTIVE,
        blank=True,
        null=True,
    )
    bonus_points = models.PositiveSmallIntegerField(_("bonus points"), blank=True, null=True, default=100)
    notes_to_client = models.TextField(_("notes to client"), blank=True, null=True)
    client_photo = models.ImageField(_("client photo"), blank=True, null=True, upload_to="media/img/client")
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    object = ClientManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("client")
        verbose_name_plural = _("clients")

    def add_bonus_point(self, points):
        """
        Adds the specified number of bonus points to the customer's account.
        """
        if self.bonus_points > 0:
            self.bonus_points += points
            self.save()
        else:
            raise ValueError("The number of points must be positive.")

    def use_bonus_points(self, points):
        """
        Withdraws the specified number of bonus points from the client's account.
        """
        if points > self.bonus_points:
            raise ValueError("You don't have enough points")
        else:
            self.bonus_points -= points
            self.save()

    def get_full_address(self):
        return f"{self.country} {self.city}"

    def send_welcome_email(self): ...  # NOQA: E704 # TODO Реализовать отправку EMAIL
