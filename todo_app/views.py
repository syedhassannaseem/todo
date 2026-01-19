from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

# Create your views here.

def addtask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        task.is_completed = True
        task.save()
        return redirect('home')
    except:
        raise Http404("Task does not exist")

def mark_as_undone(request , pk):
    try:
        task = Task.objects.get(pk=pk)
        task.is_completed = False
        task.save()
        return redirect('home')
    except:
        raise Http404("Task does not exist")
    
def edit_task(request , pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        task.task = new_task
        task.save()
        return redirect('home')
    else:
        context = {
            'task' : task
        }
        return render(request , 'edit_task.html',context)

def delete_task(request , pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')