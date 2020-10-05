from django.shortcuts import render

# Create your views here.

def view1(req):
    cbls=['topic1','topic2','topic3']
    # selebox=[]
    return render(req,'app1/app1.html',{'ls':cbls})