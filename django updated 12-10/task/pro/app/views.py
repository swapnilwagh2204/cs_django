from django.shortcuts import render
from django.http import HttpResponse
def fun1(req1):
    return render(req1,"app/first.html")
# Create your views here.
def fun2(req2):
    return HttpResponse(" app second function")
