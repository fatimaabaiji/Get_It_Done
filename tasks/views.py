# Django Imports
from django.shortcuts import render, get_object_or_404, redirect
from .forms import TaskForm
from django.contrib.auth.models import User
from .models import Task
from django.contrib import messages

# Import decorators from decorators.py
from .decorators import login_required, staff_member_required

# Create your views here.
# base.html is the main page of the website
# this function renders the base.html file
def home(request):
    return render(request, 'tasks/base.html')

# View for user dashboard, requires login
@login_required
def dashboard_view(request):
    return render(request, 'tasks/dashboard.html')

# View for admin dashboard, requires staff member
@staff_member_required
def admin_view(request):
    users = User.objects.all()
    tasks = Task.objects.all()
    return render(request, 'tasks/admin.html', {'users': users, 'tasks': tasks})

# View for editing a task, requires staff member
@staff_member_required
def edit_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task successfully edited.')
            return redirect('admin_view')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

# View for deleting a task, requires staff member
@staff_member_required
def delete_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, 'Task successfully deleted.')
    return redirect('admin_view')

# View for deleting a user, requires staff member
@staff_member_required
def delete_user_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, 'User successfully deleted.')
    return redirect('admin_view')