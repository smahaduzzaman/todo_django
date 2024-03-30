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
        if not title:
            return render(request, 'todoapp/addtodo.html', {'message': 'Please enter a title!'})
        todo = Todo.objects.create(title=title)
        todo.save()
        return redirect('addtodo')
        
    
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todoapp/addtodo.html', context)

def edittodo(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'todoapp/edittodo.html', context)

def updatetodo(request, id):
    todo = Todo.objects.get(id=id)
    title = request.POST['title']
    todo.title = title
    todo.save()
    return redirect('addtodo')
    
def deletetodo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('addtodo')
