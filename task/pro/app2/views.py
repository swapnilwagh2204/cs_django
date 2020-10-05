from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def fun21(req1):
    return HttpResponse("third app first function")
# Create your views here.
def fun22(req2):
    return render(req2,'app2/third.html')
