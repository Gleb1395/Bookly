from django.urls import path

from hotels.views import HotelListView

urlpatterns = [
    path("hotel-list/", HotelListView.as_view(), name="hotel-list"),
]
