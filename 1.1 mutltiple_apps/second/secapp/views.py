from django.shortcuts import render

from django.http.response import HttpResponse

# Create your views here.

def view1(req):
    return HttpResponse("hello world")