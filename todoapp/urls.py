from django.urls import path
from .views import index , about, addtodo, updatetodo, deletetodo

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('addtodo/', addtodo, name='addtodo'),
    path('updatetodo/<int:id>/', updatetodo, name='updatetodo'),
    path('deletetodo/<int:id>/', deletetodo, name='deletetodo')
]
