from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.filter(completed=False)
    completed_tasks = Task.objects.filter(completed=True)
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'completed_tasks': completed_tasks
        })

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            if request.user.is_authenticated:
                task.user = request.user 
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True 
    task.save()
    return redirect('task_list')
