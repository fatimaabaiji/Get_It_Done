from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from .forms import TaskForm, TaskUpdateForm, CustomUserCreationForm
from .models import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.decorators.http import require_POST
import json
from django.contrib.auth import login as auth_login

# View to create a new task
def create_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            user = form.cleaned_data.get('user')
            if not request.user.is_authenticated:
                task.user = None
                messages.warning(request, 'You are creating a task as a guest. If you are not registered, you may lose your tasks.')
                # Store task in session storage for guests
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
                task.user = request.user
                task.save()
                messages.success(request, 'Task created successfully!')
                return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

# View to display the home page with tasks
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

# View to edit an existing task
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

# View to display task details
def task_detail_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})

# View to update a task
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

# View to update the due date of a task
@csrf_exempt
@require_POST
def update_due_date_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    data = json.loads(request.body)
    due_date = data.get('due_date')
    if due_date:
        task.due_date = due_date
        task.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': 'Invalid due date'})

# View to update the priority of a task
@csrf_exempt
@require_POST
def update_priority_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    data = json.loads(request.body)
    priority = data.get('priority')
    if priority:
        task.priority = priority
        task.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': 'Invalid priority'})

# View to update the status of a task
@csrf_exempt
@require_POST
def update_status_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    data = json.loads(request.body)
    status = data.get('status')
    if status:
        task.status = status
        task.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': 'Invalid status'})

# View to log out the user
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

# View to register a new user
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

# View to log in the user
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if not request.POST.get('remember_me'):
                request.session.set_expiry(0)  # Session expires when the browser is closed
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

# View to delete a task
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.object
        return context
