from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required as django_login_required
from django.contrib.admin.views.decorators import staff_member_required as django_staff_member_required

# Custom decorator to check if the user is authenticated
def my_custom_decorator(view_func):
    def wrapper_func(request, *args, **kwargs):
        # Add your custom logic here
        if not request.user.is_authenticated:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper_func

# Alias for Django's login_required decorator
login_required = django_login_required

# Alias for Django's staff_member_required decorator
staff_member_required = django_staff_member_required