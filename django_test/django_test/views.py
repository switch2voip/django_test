# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   return render(request,'homepage.html')
