#I add this
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi, name='home-page'),
    path('add_todo/',views.add_todo), 
    path('delete_todo/<int:todo_id>/',views.delete_todo),
]