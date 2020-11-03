from django.urls import path
from .views import HomePage, AboutPage, People, Student, ContactUs
urlpatterns = [
    path('',HomePage,name='home-p'),
    path('home/',HomePage,name='home-p'),
    path('about/',AboutPage,name='about-p'),
    path('people/',People,name='people-p'),
    path('student/',Student,name='student-p'),
    path('contactus/',ContactUs,name='contactus-p'),
    
]