from django.shortcuts import render, HttpResponse
from . import views
from . models import student, postt
from .forms import studentform, postuserform
# Create your views here.


def emp(req5):
    if req5.method == 'GET':
        print("get request received")
        request = req5
        stu = studentform()
        context = {'st': stu}
        template_name = "app1/form.html"
        return render(request, template_name, context)
    else:
        print("post request received")
        r = req5.POST['rn']
        print(r)
        n = req5.POST['name']
        print(n)
        m = req5.POST['marks']
        s1 = student(rn=r, name=n, marks=m)
        s1.save()
        return HttpResponse(" record entered")


def pstusr(req6):
    if req6.method == 'GET':
        print("get request received")
        request = req6
        stu = postuserform()
        context = {'usrpst': stu}
        template_name = "app1/formpost.html"
        return render(request, template_name, context)
    else:
        print("post request received")
        con = req6.POST['content']

        cr_by = req6.POST['created_by']
        s1 = postt(content=con, created_by=cr_by)
        s1.save()
        return HttpResponse(" record entered")


def stu_dis(req):
    stu = student.objects.all()
    context = {'student': stu}
    return render(req, 'app1/stu_display.html', context)


def pstdis(req6):
    pst = postt.objects.all()
    context = {'post': pst}
    template_name = 'app1/post_display.html'
    return render(req6, template_name, context)
