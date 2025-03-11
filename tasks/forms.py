from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Task

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Username or Email", max_length=254)
    remember_me = forms.BooleanField(required=False)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date'] 