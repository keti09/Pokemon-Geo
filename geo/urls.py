from django import urls
from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.index),
    path('kanto', views.kanto),
    path('johto', views.johto),
    path('unova', views.unova)
]
