from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "urlshort"

urlpatterns = [
    path('', views.create_short_URL, name='create'),
    path('<str:pk>', views.redirect_url, name='redirect_url')
]