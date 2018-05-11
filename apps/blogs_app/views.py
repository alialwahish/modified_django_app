from django.shortcuts import render,HttpResponse,redirect
from django.template import loader

# Create your views here.
def index(request):
    
    return HttpResponse("placeholder to later display all the list of blogs")

def new(request):
    
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    
    return redirect('/')

def number(request,num):
    
    return HttpResponse('placeholder to display blog '+str(num))

def edit(request,num):
    return HttpResponse('placeholder to display EDIT blog '+str(num))

def distroy(request,num):
    return redirect('/')

