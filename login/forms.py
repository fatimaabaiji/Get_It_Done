from django import forms
from django.contrib.auth.forms import AuthenticationForm

# Custom authentication form with username/email and remember me fields
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Username or Email", max_length=254)
    remember_me = forms.BooleanField(required=False)