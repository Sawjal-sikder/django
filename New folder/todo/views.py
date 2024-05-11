from django.shortcuts import render
from .models import Todo
# Create your views here.
def todo(request):
    if request.method == 'POST':
        todo_title = request.POST.get('todo_title')
        todo_description = request.POST.get('todo_description')
        if Todo.objects.filter(todo_title=todo_title,todo_description=todo_description).exists():
            message = f'Todo title {todo_title} already exists'
        else:
             Todo.objects.create(todo_title=todo_title,todo_description=todo_description)
    all_todos = Todo.objects.all()
    return render(request, 'todo.html', locals())
