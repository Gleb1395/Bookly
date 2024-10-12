from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Hotel(models.Model):
    """
    A model to represent the hotel.
    """

    ONE_STAR = 1
    TWO_STARS = 2
    THREE_STARS = 3
    FOUR_STARS = 4
    FIVE_STARS = 5

    STARS_HOTEL_CHOICES = [
        (ONE_STAR, _("One star")),
        (TWO_STARS, _("Two stars")),
        (THREE_STARS, _("Three stars")),
        (FOUR_STARS, _("Four stars")),
        (FIVE_STARS, _("Five stars")),
    ]
    room = models.ForeignKey(
        to="hotels.Room",
        on_delete=models.CASCADE,
        null=True,
    )
    country = models.CharField(_("country"), max_length=150, blank=True, null=True)
    city = models.CharField(_("city"), max_length=150, blank=True, null=True)
    hotel_name = models.CharField(_("name"), max_length=150, blank=True, null=True)
    hotel_star_rating = models.IntegerField(_("star rating"), choices=STARS_HOTEL_CHOICES, blank=True, null=True)
    address = models.CharField(_("address"), max_length=150, blank=True, null=True)
    hotel_photo = models.ImageField(_("hotel_photo"), upload_to="media/img/hotel", blank=True, null=True)
    number_of_rooms = models.IntegerField(_("number of rooms"), blank=True, null=True)
    phone_number = PhoneNumberField(_("phone number"), blank=True, null=True)
    email = models.EmailField(_("email"), blank=True, null=True)
    website = models.URLField(_("website"), blank=True, null=True)
    description = models.TextField(_("description"), blank=True, null=True)
    client_reviews = models.TextField(_("client reviews"), blank=True, null=True)

    class Meta:
        verbose_name = _("hotel")
        verbose_name_plural = _("hotels")

    def __str__(self):
        return f"{self.hotel_name} by {self.city}"



class Room(models.Model):
    """
    A model to represent a room in a hotel.
    """

    ROOM_TYPE_CHOICES = [
        ("SGL", _("Single")),
        ("DBL", _("Double")),
        ("TWN", _("Twin")),
        ("STU", _("Studio")),
        ("APT", _("Apartment")),
        ("DEL", _("Deluxe")),
        ("FAM", _("Family")),
        ("OFF", _("Office")),
    ]

    ROOM_STATUS_CHOICES = [
        ("AVAILABLE", _("Available")),
        ("OCCUPIED", _("Occupied")),
        ("RESERVED", _("Reserved")),
        ("MAINTENANCE", _("Maintenance")),
    ]

    room_number = models.SmallIntegerField(
        _("room number"),
        null=True,
        blank=True,
        unique=True,
        validators=[
            MinValueValidator(1),
        ],
    )
    room_type = models.CharField(_("room type"), choices=ROOM_TYPE_CHOICES, null=True, blank=True, max_length=120)
    room_status = models.CharField(_("room status"), choices=ROOM_STATUS_CHOICES, null=True, blank=True, max_length=120)
    price_per_night = models.FloatField(
        _("price per night"),
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0.0),
        ],
    )
    amenities = models.ManyToManyField(to="hotels.Amenity", related_name="amenities")
    floor = models.SmallIntegerField(
        _("floor"),
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
        ],
    )
    room_description = models.TextField(_("room description"), null=True, blank=True)

    def __str__(self):
        return f"{self.room_number} {self.room_type} {self.room_status}"

    class Meta:
        verbose_name = _("room")
        verbose_name_plural = _("rooms")


class Amenity(models.Model):
    name = models.CharField(_("name"), blank=True, null=True, max_length=150)

    def __str__(self):
        return f"{self.name}"
