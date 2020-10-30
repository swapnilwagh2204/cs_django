from app1.models import postt, user, comment
from django.shortcuts import render

# Create your views here.


def view1(req1):
    stud_obj = user.objects.all()
    template_name = 'app1/index.html'
    context = {'student': stud_obj}
    return render(req1, template_name, context)


def view2(req2):
    postt_obj = postt.objects.all()
    template_name = 'app1/post.html'
    context = {'postt': postt_obj}
    return render(req2, template_name, context)


def view3(req):
    comments = comment.objects.all()
    template_name = 'app1/comment.html'
    context = {
        'comments': comments
    }
    return render(req, template_name, context)
