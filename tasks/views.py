# Django Imports
from django.shortcuts import render

# Create your views here.
#base.html is the main page of the website
#this function renders the base.html file

def home(request):
    return render(request, 'tasks/base.html')