from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
# Create your views here.
def index(request):
    tasks = Task.objects.all()[::-1]
    return render(request, 'hello/index.html', {'tasks': tasks})

def about(request):
    return render(request, 'hello/about.html')

def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'hello/create-task.html', context)