from django.shortcuts import render
from django.conf.urls import url
from . import views

urlpatterns=[
    
    url(r'^$',views.home),
    url(r'^blogs$',views.index),
    
    url(r'^blogs/new$',views.new),
    url(r'^blogs/create$',views.create),
    url(r'^blogs/(?P<num>\d+)/$',views.number),
    url(r'^blogs/(?P<num>\d+)/edit/$',views.edit),
    url(r'^blogs/(?P<num>\d+)/delete/$',views.distroy),

]
