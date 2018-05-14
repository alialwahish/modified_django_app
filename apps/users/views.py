from django.shortcuts import render

def index(request):
    word ='placeholder for users to create a new user record'
    return render(request,'users/index.html',{'word':word})

def users(request):
    
    word='placeholder to later display all the list of users'
    return render(request,'users/index.html',{'word':word})