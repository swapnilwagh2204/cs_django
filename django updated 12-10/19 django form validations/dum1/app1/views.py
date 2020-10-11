from django.shortcuts import render,HttpResponse
from . import views
from . models import student,postt
from .forms import studentform,postuserform
# Create your views here.
def emp(req5):
    if req5.method=='GET':
        print("get request received")
        request=req5
        stu=studentform()
    else:
        print("post request received")
        stu=studentform(req5.POST)
        if stu.is_valid():
            print("form is valid")
            nm=stu.cleaned_data['name']
            rn=stu.cleaned_data['rn']
            marks=stu.cleaned_data['marks']
            s1=student(rn=rn,name=nm,marks=marks)
            s1.save()
            return HttpResponse(" record entered")
    context ={'st':stu}
    template_name="app1/form.html"
    return render(req5, template_name, context)
    


def pstusr(req6):
    if req6.method=='GET':
        print("get request received")
        request=req6
        stu=postuserform()
        context ={'usrpst':stu}
        template_name="app1/formpost.html"
        return render(request, template_name, context)
    else:
        print("post request received")
        con=req6.POST['content']
      
        cr_by=req6.POST['created_by']
        s1=postt(content=con,created_by=cr_by)
        s1.save()
        return HttpResponse(" record entered")

