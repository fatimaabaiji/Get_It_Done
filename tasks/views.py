from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from .forms import TaskForm, TaskUpdateForm, CustomUserCreationForm
from .models import Task, User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

def create_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            user = form.cleaned_data.get('user')
            if user is None:
                task.user = None
                messages.warning(request, 'You are creating a task as a guest. If you are not registered, you may lose your tasks.')
                # Store task in session storage
                if 'guest_tasks' not in request.session:
                    request.session['guest_tasks'] = []
                guest_tasks = request.session['guest_tasks']
                guest_tasks.append({
                    'title': task.title,
                    'description': task.description,
                    'priority': task.priority,
                    'status': task.status,
                    'due_date': str(task.due_date),
                    'created_at': str(task.created_at),
                })
                request.session['guest_tasks'] = guest_tasks
                messages.info(request, 'Your task has been saved temporarily. Please sign up to save your progress.')
                return redirect('home')
            else:
                task.user = user
                task.save()
                messages.success(request, 'Task created successfully!')
                return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

def edit_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task edited successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Failed to edit task. Please correct the errors below.')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

def task_detail_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})

def update_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    elif request.method == 'GET':
        # Handle marking task as completed
        task.status = 'done'
        task.save()
        messages.success(request, 'Task marked as completed.')
        return redirect('home')
    return JsonResponse({'success': False, 'errors': 'Invalid request method'})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def home_view(request):
    if request.user.is_authenticated:
        priority = request.GET.get('priority')
        status_filter = request.GET.get('status_filter')
        
        tasks = Task.objects.filter(user=request.user)
        
        if priority:
            tasks = tasks.filter(priority=priority)
        
        if status_filter:
            tasks = tasks.filter(status=status_filter)
        
        tasks = tasks.order_by('-priority', 'status')  # Order by priority in descending order and status
        
        guest_tasks = []
    else:
        tasks = []
        guest_tasks = request.session.get('guest_tasks', [])
        if not guest_tasks:
            guest_tasks = [
                {
                    'title': 'Example Task 1',
                    'description': 'This is an example task.',
                    'priority': 'medium',
                    'status': 'not_started',
                    'due_date': '2025-12-31',
                    'created_at': '2025-01-01 00:00:00',
                },
                {
                    'title': 'Example Task 2',
                    'description': 'This is another example task.',
                    'priority': 'high',
                    'status': 'in_progress',
                    'due_date': '2025-12-31',
                    'created_at': '2025-01-01 00:00:00',
                },
            ]
        # Sort guest tasks by priority and status
        guest_tasks = sorted(guest_tasks, key=lambda x: (x['status'] == 'done', x['priority'] == 'low', x['priority'] == 'medium', x['priority'] == 'high'))
    return render(request, 'tasks/home.html', {'tasks': tasks, 'guest_tasks': guest_tasks})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email_user(
                subject='Registration Confirmation',
                message='Thank you for registering. Please confirm your email address.',
                from_email='noreply@example.com'
            )
            messages.success(request, 'Registration successful. Please check your email for confirmation.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.object
        return context

