from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")
def kareem(request):
    return HttpResponse("Hello, Kareem!")
def greet(request, name):
     return HttpResponse(f"Hello, {name}!")