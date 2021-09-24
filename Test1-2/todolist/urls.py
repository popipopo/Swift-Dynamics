from django.urls import path
from . import views

app_name = "todolist" # keep any name or app name
urlpatterns=[
    path("",views.index,name="index"),
    path("add",views.add,name="add"),
    path("remove",views.remove,name="remove"),
    path("edit",views.edit,name="edit"),
]