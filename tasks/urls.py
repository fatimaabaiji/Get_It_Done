from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('create-task/', views.create_task_view, name='create_task'),
    path('update-task-status/<int:task_id>/<str:status>/', views.update_task_status_view, name='update_task_status'),
    path('delete-task/<int:task_id>/', views.delete_task_view, name='delete_task'),
    path('edit-task/<int:task_id>/', views.edit_task_view, name='edit_task'),  # Add this line
]