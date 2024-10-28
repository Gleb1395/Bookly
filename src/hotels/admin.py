from django.contrib import admin

from hotels.models import Hotel, Room


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = [
        "country",
        "city",
        "hotel_name",
        "hotel_star_rating",
        "address",
        "hotel_photo",
        "number_of_rooms",
        "phone_number",
        "email",
        "website",
        "description",
        "client_reviews",
    ]


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = [
        "room_number",
        "room_type",
        "room_status",
        "price_per_night",
        # "amenities",
        "floor",
        "room_description",
    ]
