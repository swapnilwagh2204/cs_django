from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class student:
    def __init__(self,rn,nm,marks):
        self.rn = rn
        self.nm = nm
        self.marks = marks

    def __str__(self):
        return "{},{},{}".format(self.rn,self.nm,self.marks)


s1=student(1,'radha',26)
s2=student(2,'priya',29)
s3=student(3,'jay',30)
def ls(req1):
    context={'s':[s1,s2,s3],'ele':[[1,'radha',260],[2,'priya',29],[3,'jay',30]],'val':[1,2,3]}
    request=req1
    template_name='app1/index.html'
    return render(request,template_name,context)

def dct(req2):
    context ={'student_date':{'s1':{'rn':1,'nm':'radha','marks':26},'s2':{'rn':2,'nm':'priya','marks':29,'s3':{'rn':3,'nm':'jay','marks':30}}}}
    request=req2
    template_name='app1/index.html'

    return render(request, template_name,context)


def st(req3):
    context={'s':[s1,s2,s3],'ele':{frozenset({1,'radha',26}),frozenset({2,'priya',29,}),frozenset({3,'jay',30})}}
    request=req3
    template_name="app1/index.html"
    return render(request, template_name, context) 

def lod(req4):
    lsd =[{'rn':1,'nm':'radha','marks':26},{'rn':2,'nm':'priya','marks':29},{'rn':3,'nm':'jay','marks':30}]
    request=req4
    template_name="app1/index.html"
    return render(request, template_name,{'ld':lsd}) 


def dol(req5):
    context={[1,'radha',260],[2,'priya',29],[3,'jay',30]}
    request=req5
    template_name='app1/index.html'
    return render(request,template_name,context)
