from django.urls import path

from . import views

app_name = 'getweather'
urlpatterns = [
    path('', views.index, name='index'),
    path('sity/', views.sity, name='sity'),
]