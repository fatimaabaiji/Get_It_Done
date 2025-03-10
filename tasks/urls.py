# filepath: c:\Users\fatima\Desktop\git-it-done\Get_It_Done\tasks\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]