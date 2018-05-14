from django.shortcuts import render,redirect

word="placeholder to display all the surveys created"

def index(request):
    word="placeholder to display all the surveys created"
    return render(request,'surveyApp/index.html',{'word':word})

def new(request):
    word="placeholder for users to add a new survey"
   
    return render(request,'surveyApp/index.html',{'word':word})