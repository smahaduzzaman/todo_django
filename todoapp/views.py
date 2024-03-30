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

def updatetodo(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST['title']
        if not title:
            return render(request, 'todoapp/updatetodo.html', {'todo': todo, 'message': 'Please enter a title!'})
        todo.title = title
        todo.save()
        return render(request, 'todoapp/updatetodo.html', {'todo': todo, 'message': 'Todo updated successfully!'})
    context = {
        'todo': todo
    }
    return render(request, 'todoapp/updatetodo.html', context)
    
def deletetodo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('addtodo')
