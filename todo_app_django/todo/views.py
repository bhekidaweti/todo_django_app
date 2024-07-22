from django.shortcuts import render, redirect, get_object_or_404
from . models import Todo
# Create your views here.

def index(request):
    tasks = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': tasks})

def create_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task')
        task_description = request.POST.get('description')
        task = Todo.objects.create(task=task_name, description=task_description)
        task.save()
        return redirect('index')
    
def delete_task(request, todo_id):
    task = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        task.delete()    
        return redirect('index')

        
