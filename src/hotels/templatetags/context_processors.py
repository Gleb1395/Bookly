from hotels.models import Hotel


def country_context(request):
    hotels = Hotel.objects.all()
    return {"hotels": hotels}
