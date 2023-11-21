from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')

def experience(request):
    return HttpResponse('experience.')
def projects(request):
    return HttpResponse('projects.')
def certifications(request):
    return HttpResponse('certifications.')
def contact(request):
    return HttpResponse('contact.')

def test(request):
    return HttpResponse('<h1><center>working...</center></h1>')

