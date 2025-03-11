# Django Imports
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm, TaskForm # from forms.py
from django.contrib.auth.models import User
from .models import Task  # Assuming you have a Task model
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

# Create your views here.
#base.html is the main page of the website
#this function renders the base.html file

def home(request):
    return render(request, 'tasks/base.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('dashboard')
        else:
            error_message = "Invalid username or password."
    else:
        form = CustomAuthenticationForm()
        error_message = None
    return render(request, 'tasks/login.html', {'form': form, 'error_message': error_message})

@login_required
def dashboard_view(request):
    return render(request, 'tasks/dashboard.html')

@staff_member_required
def admin_view(request):
    users = User.objects.all()
    tasks = Task.objects.all()
    return render(request, 'tasks/admin.html', {'users': users, 'tasks': tasks})

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

@staff_member_required
def delete_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, 'Task successfully deleted.')
    return redirect('admin_view')