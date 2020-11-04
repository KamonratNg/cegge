from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentRecord

# Create your views here.
def HomePage(request):
    return render(request,'ce/home.html')

def AboutPage(request):
    return render(request,'ce/about.html')

def ContactUs(request):
    return render(request,'ce/contactus.html')

def People(request):
    return render(request,'ce/people.html')

#this page show data from models
def Student(request):
    student_ID = StudentRecord.objects.all() 
    #pull data from models
    context = {'student_ID':student_ID}
    return render(request,'ce/student.html',context)    

def Register(request):
    return render(request,'ce/register.html')