from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view1(req1):
    return HttpResponse("hello world from secapp1")

def view11(req11):
    return HttpResponse("hello world 21 from secapp1")
