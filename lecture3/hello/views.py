from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")
def kareem(request):
    return HttpResponse("Hello, Kareem!")
def greet(request):
     return HttpResponse(f"Hello, {name}1")