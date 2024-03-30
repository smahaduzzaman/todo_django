from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    return render(request, 'todoapp/index.html')

def about(request):
    return render(request, 'todoapp/about.html')

def addtodo(request):
    if request.method == 'POST':
        title = request.POST['title']
        todo = Todo.objects.create(title=title)
        todo.save()
        return render(request, 'todoapp/addtodo.html', {'message': 'Todo added successfully!'})
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todoapp/addtodo.html', context)
