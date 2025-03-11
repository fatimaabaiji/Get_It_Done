from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import CustomAuthenticationForm

# View for user login
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('dashboard')
        else:
            error_message = "Invalid username or password."
    else:
        form = CustomAuthenticationForm()
        error_message = None
    return render(request, 'login/login.html', {'form': form, 'error_message': error_message})
