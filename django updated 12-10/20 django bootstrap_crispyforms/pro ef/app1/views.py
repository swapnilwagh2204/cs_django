from django.shortcuts import redirect, render
from django.http import request
from. forms import studentform
from .models import student
# Create your views here.

def home(req2):
    context ={}
    request=req2
    template_name='app1/home.html'

    return render(request, template_name,context)

def about(req2):
    context ={}
    request=req2
    template_name='app1/about.html'

    return render(request, template_name,context)

def contact(req3):
    context ={}
    request=req3
    template_name='app1/contact.html'

    return render(request, template_name,context)

def info(req4):
    context ={}
    request=req4
    template_name='app1/info.html'

    return render(request, template_name,context)


def addstu(request):
    if request.method=='GET':
        print("get method received")
        form=studentform()
    else:
        print("post method received")
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            print("data inserted,redirecting to dispstudent")
            return redirect('disstu')
    template_name='app1/addstudent.html'
    context={'form':form}
    return render(request, template_name,context)

def disstu(request):
    obj=student.objects.all()
    template_name='app1/dispstudent.html'
    context={'students':obj}
    return render(request, template_name, context)

