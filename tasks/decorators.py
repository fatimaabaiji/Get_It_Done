
from django.http import HttpResponse
from django.shortcuts import redirect

def my_custom_decorator(view_func):
    def wrapper_func(request, *args, **kwargs):
        # Add your custom logic here
        if not request.user.is_authenticated:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper_func