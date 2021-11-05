from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.views import generic
from forms import SityForm
import requests
import pyowm
from pyowm import OWM


def index(request):
    sity_form = SityForm()
    return render(request, 'getweather/index.html', {'form': sity_form})


def sity(request):
    if request.method == "POST":
        sity_name = request.POST.get("your_sity")
        owm = OWM('8a16d827038565e2a5343120d3e8b698')
        mgr = owm.weather_manager()
        try:
            observation = mgr.weather_at_place(sity_name)
        except:
            raise Http404("Sity does not exist")

        w = observation.weather

        context = {
            'sity': sity_name,
            'temp': w.temperature('celsius')['temp'],
            'feels_like': w.temperature('celsius')['feels_like'],
            'description': w.detailed_status,
            'humidity': w.humidity,
            'clouds': w.clouds,
            'wind': w.wind()['speed']


        }
        return render(request, 'getweather/sity.html', context=context)
