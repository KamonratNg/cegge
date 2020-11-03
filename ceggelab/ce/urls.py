from django.urls import path
from .views import HomePage, AboutPage, ContactUs
urlpatterns = [
    path('',HomePage,name='home'),
    path('home/',HomePage,name='home'),
    path('about/',AboutPage,name='about'),
    path('contactus/',ContactUs,name='contactus')
]