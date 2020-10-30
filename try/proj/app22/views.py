from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'app22/index1.html')


def info(request):
    return render(request, 'app22/info1.html')


def msg(request):
    return render(request, 'app22/msg.html')
