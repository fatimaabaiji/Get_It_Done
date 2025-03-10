# filepath: c:\Users\fatima\Desktop\git-it-done\Get_It_Done\tasks\views.py
from django.shortcuts import render

def home(request):
    return render(request, 'tasks/base.html')
