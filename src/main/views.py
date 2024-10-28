from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from hotels.models import Hotel


class IndexView(TemplateView):
    template_name = "index.html"
