from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def HomePage(request):
    return render(request,'ce/home.html')

def AboutPage(request):
    return render(request,'ce/about.html')

def ContactUs(request):
    return render(request,'ce/contactus.html')

def People(request):
    return render(request,'ce/people.html')

def Student(request):
    return render(request,'ce/student.html')    