from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'todoapp/index.html')

def about(request):
    return render(request, 'todoapp/about.html')

def addtodo(request):
    return render(request, 'todoapp/addtodo.html')