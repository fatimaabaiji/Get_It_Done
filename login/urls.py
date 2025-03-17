from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Ensure this URL pattern is named 'home'
    path('tasks/delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete_task'),
    # Other URLs...
]
