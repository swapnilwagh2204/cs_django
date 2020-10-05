from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse
def view2(req2):
    return HttpResponse("HELLO WORLD FROM VIEW2 APP 2")


def view21(req21):
    return HttpResponse("HELLO WORLD 21 FROM VIEW21 APP 2")