from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from hotels.models import Hotel


class IndexView(TemplateView):
    template_name = "index.html"

