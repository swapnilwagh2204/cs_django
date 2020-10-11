from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def view1(req1):
    return HttpResponse("this is HttpResponse 1")

def view2(req2):
    return HttpResponse("this is HttpResponse 2")


def view3(req3):
    return render(req3,'third.html')

def view4(req4):
    return render(req4,'fourth.html')