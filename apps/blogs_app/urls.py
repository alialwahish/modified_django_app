from django.shortcuts import render
from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns=[
    url(r'^$',views.index),
    url(r'^new/$',views.new),
    url(r'^create$',views.create),
    url(r'^(?P<num>\d+)/$',views.number),
    url(r'^(?P<num>\d+)/edit/$',views.edit),
    url(r'^(?P<num>\d+)/delete/$',views.distroy),

]
