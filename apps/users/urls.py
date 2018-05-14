from django.shortcuts import render,HttpResponse, redirect
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'register',views.index),
    url(r'^users$',views.users),
    url(r'^users/new$',views.index),
]