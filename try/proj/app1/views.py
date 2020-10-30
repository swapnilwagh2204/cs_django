from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'app1/index1.html')


def info(request):
    return render(request, 'app1/info1.html')


def msg(request):
    return render(request, 'app1/msg.html')
