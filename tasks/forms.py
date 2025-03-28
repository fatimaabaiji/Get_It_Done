from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Task

# Custom authentication form with username/email and remember me fields
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Username or Email", max_length=254)
    remember_me = forms.BooleanField(required=False)

# Form for creating and editing tasks
class TaskForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False, empty_label="Guest")

    class Meta:
        model = Task
        fields = ['title', 'description', 'user', 'priority', 'due_date', 'status']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_user(self):
        user = self.cleaned_data.get('user')
        if user is None:
            return None
        return user

# Form for updating tasks
class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['priority', 'status']

# Registration form for new users with password validation
class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Username", max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    # Custom validation to ensure passwords match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

# Custom user creation form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']