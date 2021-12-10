from django.urls import path
from . import views

app_name = "addVote" #specifies that a url name refers to the tasks app (see add.html for implementation)
urlpatterns = [
    path("", views.index, name="index"),
    path("addNew", views.add, name="addNew")
]