from app1.models import postt, student
from django.shortcuts import render, HttpResponse

# Create your views here.


def view1(req1):
    stud_obj = student.objects.all()
    template_name = 'app1/stu_display.html'
    context = {'student': stud_obj}
    return render(req1, template_name, context)


def view2(req2):
    postt_obj = postt.objects.all()
    template_name = 'app1/post_display.html'
    context = {'postt': postt_obj}
    return render(req2, template_name, context)


def insertdata(request1):
    if request1.method == 'GET':
        print("get request received")
        request = request1
        context = {}
        template_name = "app1/stu_entry.html"
        return render(request, template_name, context)
    else:
        print("post request received")
        rn = request1.POST['r']
        name = request1.POST['n']
        marks = request1.POST['m']
        s1 = student(rn=rn, name=name, marks=marks)
        s1.save()
        return HttpResponse(" record entered")

        # return HttpResponse(f"{rn} {name} {marks}")


def insertpost(req):
    if req.method == "GET":
        print("get request received")
        context = {}
        template_name = "app1/post_entry.html"
        # return HttpResponse("entry done")
        return render(req, template_name, context)
    else:
        print("post request received")
        content = req.POST['txt']
        created_by = req.POST['cr']
        s2 = postt(content=content, created_by=created_by)
        s2.save()
        return HttpResponse(" record entered")
        # return HttpResponse(f"{content}\n{created_by}")
