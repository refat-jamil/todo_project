from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks, 'form':form})

def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_complete = not task.is_complete  # Toggle completion status
    task.save()
    return redirect('home')


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_edit.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, 'task_confirm_delete.html', {'task': task})
