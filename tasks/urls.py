from django.urls import path
from . import views
from .views import TaskDeleteView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create-task/', views.create_task_view, name='create_task'),
    path('update-task/<int:task_id>/', views.update_task_view, name='update_task'),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),
    path('edit-task/<int:task_id>/', views.edit_task_view, name='edit_task'),
    path('task/<int:task_id>/', views.task_detail_view, name='task_detail'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('update-due-date/<int:task_id>/', views.update_due_date_view, name='update_due_date'),
    path('update-priority/<int:task_id>/', views.update_priority_view, name='update_priority'),
    path('update-status/<int:task_id>/', views.update_status_view, name='update_status'),
]