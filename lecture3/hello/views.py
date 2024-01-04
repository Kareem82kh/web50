from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(rerquest):
    return HttpResponse("Hello, `world! Thia is my First Django app")