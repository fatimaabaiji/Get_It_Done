from django.urls import path, include
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Include login and register app URLs
    path('', include('login.urls')),
    path('', include('register.urls')),

    # User dashboard, requires login
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Admin dashboard, requires staff member
    path('admin/', views.admin_view, name='admin_view'),
    path('admin/edit-task/<int:task_id>/', views.edit_task_view, name='edit_task'),
    path('admin/delete-task/<int:task_id>/', views.delete_task_view, name='delete_task'),
]