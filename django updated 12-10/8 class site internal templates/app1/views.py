from django.shortcuts import render
from django.http import request

# Create your views here.
class student:
    def __init__(self,rn,nm,marks,image):
        self.rn = rn
        self.nm = nm
        self.marks = marks
        self.image = image

    def __str__(self):
        return "{},{},{}".format(self.rn,self.nm,self.marks,self.image)


s1=student(1,'swapnil',100,'/static/images/ai.jpg')
s2=student(2,'sss',200,'/static/images/backg.jpg')
s3=student(3,'waaa',300,'/static/images/2states1.png')

def home(req2):
    context ={'ls1':{'hm':'home','cn':'contact','ab':'about'},'ss':[s1,s2,s3]}
    request=req2
    template_name='home.html'

    return render(request, template_name,context)

def about(req2):
    context ={'ss':[s1,s2,s3]}
    request=req2
    template_name='about.html'

    return render(request, template_name,context)

def contact(req3):
    context ={'ss':[s1,s2,s3]}
    request=req3
    template_name='contact.html'

    return render(request, template_name,context)

def info(req4):
    context ={'ss':[s1,s2,s3]}
    request=req4
    template_name='info.html'

    return render(request, template_name,context)

