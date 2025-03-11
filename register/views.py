from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib.auth import get_backends
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# View for user registration
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Specify the backend to use for authentication
            backend = get_backends()[0]
            user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
            login(request, user)
            messages.success(request, 'Registration successful! A confirmation email has been sent.')
            # Send confirmation email
            send_mail(
                'Registration Confirmation',
                'Thank you for registering at Get It Done.',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            return redirect('dashboard')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = RegistrationForm()
    return render(request, 'register/register.html', {'form': form})
