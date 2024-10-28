from django.shortcuts import render
from django.views.generic import ListView

from hotels.models import Hotel


class HotelListView(ListView):
    model = Hotel
    context_object_name = 'hotels'
    template_name = "hotel_list.html"
    paginate_by = 12






