from django.urls import path
from .views import index , about, addtodo

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('addtodo/', addtodo, name='addtodo')
]
