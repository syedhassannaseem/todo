from django.shortcuts import render
from todo_app.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed= False).order_by('-updated_at') # if we write 'update_at' then it will move in ascending order and we use '-' then it will move in descending order
    completed_tasks = Task.objects.filter(is_completed = True)
    context = {
        "tasks" : tasks,
        "completed_tasks" : completed_tasks
    }
    return render(request , 'home.html',context)