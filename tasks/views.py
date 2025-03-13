# Django Imports
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import TaskForm
from .models import Task

# Create your views here.
# base.html is the main page of the website
# this function renders the base.html file
def home(request):
    return render(request, 'tasks/base.html')

# View for creating a task, requires login
@login_required
def create_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created successfully.')
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

@login_required
def update_task_status_view(request, task_id, status):
    task = get_object_or_404(Task, id=task_id)
    if task.user == request.user:
        task.status = status
        task.save()
        messages.success(request, f'Task status updated to {status}.')
    else:
        messages.error(request, 'You do not have permission to update this task.')
    return redirect('home')

@login_required
def delete_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if task.user == request.user:
        task.delete()
        messages.success(request, 'Task deleted successfully.')
    else:
        messages.error(request, 'You do not have permission to delete this task.')
    return redirect('home')

@login_required
def edit_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if task.user != request.user:
        messages.error(request, 'You do not have permission to edit this task.')
        return redirect('home')
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully.')
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/edit_task.html', {'form': form})

def home_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['task_created'] = True
    else:
        form = TaskForm()
        request.session['task_created'] = False
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {'form': form, 'tasks': tasks})
