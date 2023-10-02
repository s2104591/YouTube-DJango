from django.shortcuts import render
from .models import Student

# Create your views here.

def myviewfunct(request):
    return render(request,"child.html")



def studentsfunct(request):
    studentslist= Student.objects.all()
    return render(request,"students.html",  {"students" : studentslist} )







