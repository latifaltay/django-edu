# tcore/urls.py
from django.urls import path
from .views import index, about, merhaba, welcome_user, website_info, website_home

urlpatterns = [
    path('', index, name="index"),
    path('about', about, name="about"),
    path('merhaba', merhaba, name="merhaba"),
    path('welcome_user', welcome_user, name='welcome_user'),
    path('website_info', website_info, name='website_info'),
    path('home', website_home, name='home')
]
