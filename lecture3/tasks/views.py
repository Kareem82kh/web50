from django.shortcuts import render
from django import forms

tasks = [ "Task1", "Task2", "Task3"]

class NewTaskForm(forms.Form):
    task =forms.CharField(lable="New Task")
# Create your views here.
def index(request):
    return render (request, "tasks/index.html", {
        "tasks": tasks
    })
def add(request):
    return render(request, "tasks/add.html"), {
        "form": NewTaskForm()
    }