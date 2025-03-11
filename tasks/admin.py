from django.contrib import admin

# Import your models here
from .models import Task

# Register your models here.
# This allows the Task model to be managed through the Django admin interface
admin.site.register(Task)
