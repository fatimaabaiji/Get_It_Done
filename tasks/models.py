# filepath: c:\Users\fatima\Desktop\git-it-done\tasks\models.py
from django.db import models
from django.contrib.auth.models import User

# Task model to represent a task in the application
class Task(models.Model):
    # Choices for task priority
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    # Choices for task status
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    
    # Fields for the Task model
    title = models.CharField(max_length=255)  # Title of the task
    description = models.TextField()  # Description of the task
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # User who created the task
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)  # Priority of the task
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)  # Status of the task
    due_date = models.DateField()  # Due date of the task
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the task was created

    def __str__(self):
        return self.title  # String representation of the task
