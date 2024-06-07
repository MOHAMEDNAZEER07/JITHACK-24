from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('input', views.input, name='input'),
    path('crop', views.crop, name='crop'),
]