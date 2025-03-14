from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create-task/', views.create_task_view, name='create_task'),
    path('update-task/<int:task_id>/', views.update_task_view, name='update_task'),
    path('delete-task/<int:task_id>/', views.delete_task_view, name='delete_task'),
    path('edit-task/<int:task_id>/', views.edit_task_view, name='edit_task'),
]