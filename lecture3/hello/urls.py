from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("kareem", views.kareem, name="kareem"),
    path("<str:name>", views.greet, name="greet"),
]