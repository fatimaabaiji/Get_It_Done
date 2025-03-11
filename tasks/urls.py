from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Login page
    path('login/', views.login_view, name='login'),

    # User dashboard, requires login
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Admin dashboard, requires staff member
    path('admin/', views.admin_view, name='admin_view'),

    # Edit task page, requires staff member
    path('admin/edit-task/<int:task_id>/', views.edit_task_view, name='edit_task'),

    # Delete task page, requires staff member
    path('admin/delete-task/<int:task_id>/', views.delete_task_view, name='delete_task'),

    # User registration page
    path('register/', views.register_view, name='register'),
]