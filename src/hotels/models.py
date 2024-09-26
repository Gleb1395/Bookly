from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Hotel(models.Model):
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
    # room =...
