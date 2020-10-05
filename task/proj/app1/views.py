from django.shortcuts import render

# Create your views here.

def view1(req):
    return render(req,'app1/home.html')


def view2(req):
    return render(req,'app1/about.html')
def view3(req):
    return render(req,'app1/contact.html')
def view4(req):
    return render(req,'app1/info.html')