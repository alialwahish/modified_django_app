from django.shortcuts import render,HttpResponse,redirect
from django.template import loader

# Create your views here.
def home(request):
    return redirect('/blogs')

def index(request):
    word="placeholder to later display all the list of blogs"
    return render(request,'blogs_app/index.html',{'word':word})
        

def new(request):
    
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    
    return redirect('/blogs')

def number(request,num):
    
    return HttpResponse('placeholder to display blog '+str(num))

def edit(request,num):
    return HttpResponse('placeholder to display EDIT blog '+str(num))

def distroy(request,num):
    return redirect('/blogs')

