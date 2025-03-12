from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# View for user registration
def register_view(request):
    registration_success = False
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful! A confirmation email has been sent.')
            # Send confirmation email
            send_mail(
                'Registration Confirmation',
                'Thank you for registering at Get It Done.',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            registration_success = True
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = RegistrationForm()
    return render(request, 'register/register.html', {'form': form, 'registration_success': registration_success})
