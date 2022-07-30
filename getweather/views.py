from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.views import generic
from forms import SityForm
import requests
import pyowm
from pyowm import OWM
import json


def index(request):
    sity_form = SityForm()
    return render(request, 'getweather/index.html', {'form': sity_form})


def check_city(city):
    city_wl = city.replace('-', '')
    cities = {"saintpetersburg": "saint petersburg", "rostovondon": "rostov-on-don", "nizhnynovgorod": "nizhny novgorod"}
    if city_wl in cities:
        return cities[city_wl]
    else:
        return city



def sity(request, *args, **kwargs):
    if request.method == "POST":
        sity_name = request.POST.get("your_sity")
        sity_name = check_city(sity_name)
        owm = OWM('8a16d827038565e2a5343120d3e8b698')
        mgr = owm.weather_manager()
        try:
            observation = mgr.weather_at_place(sity_name)
        except:
            raise Http404("City does not exist")

        w = observation.weather
        sity_form = SityForm()
        context = {
            'sity': sity_name,
            'temp': w.temperature('celsius')['temp'],
            'feels_like': w.temperature('celsius')['feels_like'],
            'description': w.detailed_status,
            'humidity': w.humidity,
            'clouds': w.clouds,
            'wind': w.wind()['speed'],
            'form': sity_form,


        }

        return render(request, 'getweather/sity.html', context=context)


def city(request, slug):
    city_name = request.POST.get("your_sity")
    if slug:
        city_name = slug
    city_name = check_city(city_name)
    owm = OWM('8a16d827038565e2a5343120d3e8b698')
    mgr = owm.weather_manager()
    try:
        observation = mgr.weather_at_place(city_name)
    except:
        raise Http404("City does not exist")

    w = observation.weather
    sity_form = SityForm()
    context = {
        'sity': city_name,
        'temp': w.temperature('celsius')['temp'],
        'feels_like': w.temperature('celsius')['feels_like'],
        'description': w.detailed_status,
        'humidity': w.humidity,
        'clouds': w.clouds,
        'wind': w.wind()['speed'],
        'form': sity_form,
    }
    return render(request, 'getweather/sity.html', context=context)


def about(request):
    sity_form = SityForm()
    return render(request, 'getweather/about.html', {'form': sity_form})


def mailpost(request):
    sity_form = SityForm()
    return render(request, 'getweather/mailpost.html', {'form': sity_form})
