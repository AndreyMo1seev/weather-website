from django.urls import path

from . import views

app_name = 'getweather'
urlpatterns = [
    path('', views.index, name='index'),
    path('sity/', views.sity, name='sity'),
    path('sity/<slug:slug>/', views.city, name='city'),
    path('about/', views.about, name='about'),
    path('mailpost/', views.mailpost, name='mailpost'),
]