from django.http.response import HttpResponse
from django.shortcuts import render
from .models import student, postt
# Create your views here.


def home(request):
    return HttpResponse('this is home page')


def view1(request):
    stu = student.objects.all()
    context = {'student': stu}
    template_name = "app1/student.html"
    return render(request, template_name, context)


def view2(request):
    pos = postt.objects.all()
    context = {
        'pos': pos
    }
    template_name = 'app1/post.html'
    return render(request, template_name, context)
