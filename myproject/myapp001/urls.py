from django.urls import path
from . import views

urlpatterns=[
    path("myview/", views.myviewfunct, name="v1"),
    path("", views.myviewfunct,name="v2"),
    path("students/", views.studentsfunct,name="v3")


]


