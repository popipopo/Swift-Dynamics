from django.urls import path
from . import views

app_name = "send_mail" # keep any name or app name
urlpatterns=[
    path("",views.index,name="index"),
    path("sendmail",views.sendmail,name="sendmail")
]