# task/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm

@login_required
def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('index')
        else:
            # If form is invalid, show errors
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TaskForm()
    
    tasks = Task.objects.filter(owner=request.user).order_by('-timestamps')
    
    # Debug: Print form info
    print(f"Form object: {form}")
    print(f"Form fields: {form.fields if form else 'No form'}")
    
    return render(request, 'index.html', {'tasks': tasks, 'form': form})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'edit_task.html', {'form': form, 'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, owner=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('index')
    return render(request, 'delete_task.html', {'task': task})

@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, owner=request.user)
    task.status = not task.status
    task.save()
    return JsonResponse({'status': task.status})

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

def custom_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('login')
