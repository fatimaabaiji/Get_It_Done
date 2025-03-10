# Django Imports
from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm

# Create your views here.
#base.html is the main page of the website
#this function renders the base.html file

def home(request):
    return render(request, 'tasks/base.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if form.cleaned_data.get('remember_me'):
                request.session.set_expiry(1209600)  # 2 weeks
            return redirect('dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'tasks/dashboard.html')