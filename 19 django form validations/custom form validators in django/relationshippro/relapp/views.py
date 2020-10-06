from django.shortcuts import render
from django.http import HttpResponse
from .models import EmpReg
from .forms import EmpForm
# Create your views here.


def empRegView(request):
    template_name = 'relapp/reg.html'

    if request.method == 'GET':
        form = EmpForm()
        return render(request,template_name,{'form':form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data.get('username')
            p = form.cleaned_data.get('password')
            fn = form.cleaned_data.get('fullname')
            ad = form.cleaned_data.get('address')
            g = form.cleaned_data.get('gender')
            c = form.cleaned_data.get('city')

            emp = EmpReg(username=u,password=p,fullname=fn,address=ad,gender=g,city=c)
            emp.save()
            return render(request,'relapp/login.html')
        return render(request,template_name,{'form':form})



def loginView(request):
    return HttpResponse("Hello")