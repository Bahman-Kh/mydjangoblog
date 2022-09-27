from django.shortcuts import render
from django.shortcuts import HttpResponse

def info(request):
    #return HttpResponse('About Page')
    return render(request, 'info.html')

def home(request):
    #return HttpResponse('Home Page')
    return render(request, 'home.html')
