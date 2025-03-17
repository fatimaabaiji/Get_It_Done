from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create-task/', views.create_task_view, name='create_task'),
    path('update-task/<int:task_id>/', views.update_task_view, name='update_task'),
    path('tasks/delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete_task'),
    path('edit-task/<int:task_id>/', views.edit_task_view, name='edit_task'),
    path('task/<int:task_id>/', views.task_detail_view, name='task_detail'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]