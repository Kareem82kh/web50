from django.shortcuts import render

tasks = [ "Task1, "Task2", "Task3"]

# Create your views here.
def index(request):
    return render (request, "tasks/index.html", {
        "tasks": tasks
    })