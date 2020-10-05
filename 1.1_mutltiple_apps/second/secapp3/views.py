from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def view3(req3):
    return HttpResponse("hello world from app 3")

def view31(req31):
    return HttpResponse("hello world from app 31")