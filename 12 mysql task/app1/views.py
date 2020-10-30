from django.shortcuts import render

# Create your views here.


def view1(req1):
    return render(req1, 'app1/index.html')
