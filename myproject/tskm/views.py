
from django.shortcuts import render, redirect
from .models import Task

# Task List View
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tskm/task_list.html', {'tasks': tasks})

# Task Create View
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'tskm/task_create.html')
 