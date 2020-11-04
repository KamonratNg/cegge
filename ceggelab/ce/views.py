from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Studentrecord
from django.contrib.auth.models import User

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
    student_ID = Studentrecord.objects.all() 
    #pull data from models
    context = {'student_ID':student_ID}
    return render(request,'ce/student.html',context)    

def Register(request):

    if request.method == 'POST':
        data = request.POST.copy()
        firstname = data.get('firstname')
        lastname= data.get('lastname')
        email = data.get('email')
        pwd = data.get('pwd')

        newuser = User()
        newuser.username = email
        newuser.firstname = firstname
        newuser.lastname = lastname
        newuser.email=email
        newuser.set_password(pwd)
        newuser.save()
        return redirect('home-p')

    return render(request,'ce/register.html')