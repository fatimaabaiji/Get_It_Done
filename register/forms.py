from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

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