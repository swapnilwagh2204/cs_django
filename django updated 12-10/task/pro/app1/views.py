
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
def fun11(req1):
    return HttpResponse("first app first function")
# Create your views here.
def fun12(req2):
    return render(req2,'app2/second.html')
