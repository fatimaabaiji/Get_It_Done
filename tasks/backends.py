from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

# Get the user model
User = get_user_model()

# Custom authentication backend to allow login with either email or username
class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # If username is not provided, get it from kwargs
        if username is None:
            username = kwargs.get('username')
        # If username or password is still not provided, return None
        if username is None or password is None:
            return
        try:
            # Try to get the user by email
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                # If user is not found by email, try to get the user by username
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # If user is not found by either email or username, return None
                return
        # Check if the provided password is correct and the user can authenticate
        if user.check_password(password) and self.user_can_authenticate(user):
            return user