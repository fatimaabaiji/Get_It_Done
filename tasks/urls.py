from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('admin/', views.admin_view, name='admin_view'),
    path('admin/edit-task/<int:task_id>/', views.edit_task_view, name='edit_task'),
    path('admin/delete-task/<int:task_id>/', views.delete_task_view, name='delete_task'),
    path('register/', views.register_view, name='register'),
]