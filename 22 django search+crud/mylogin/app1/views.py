from django.http import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import regForm, postuserform, postupdateform
from .models import Users, postt
from . import views


def empRegView(request):
    template_name = 'app1/register.html'

    if request.method == 'GET':
        form = regForm()
        return render(request, template_name, {'form': form})
    else:
        form = regForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data.get('username')
            p = form.cleaned_data.get('password')
            fn = form.cleaned_data.get('fullname')
            ad = form.cleaned_data.get('address')
            g = form.cleaned_data.get('gender')

            emp = Users(Username=u, Password=p,
                        Fullname=fn, Address=ad, Gender=g)
            emp.save()
            return render(request, 'app1/login.html')
        return render(request, template_name, {'form': form})


def loginview(request):
    if request.method == 'GET':
        template_name = "app1/login.html"
        return render(request, template_name)
    else:
        u = request.POST['username']
        p = request.POST['password']
        if Users.objects.get(Username=u, Password=p):

            posts = postt.objects.filter(overview__Username=u)
            context = {"us": posts}
            return render(request, "app1/display.html", context)
        return render(request, "app1/login.html")


def deleteview(request, pk):
    try:
        data = postt.objects.get(pk=pk)
        if request.method == 'GET':
            context = {'obj': data}
            template_name = "app1/delete.html"
            return render(request, template_name, context)
        else:
            data.delete()
            return redirect('register')
    except:
        return HttpResponse("please provide valid input")


def updateview(request, pk):
    try:
        data = postt.objects.get(pk=pk)
        if request.method == 'GET':
            form = postupdateform(instance=data)
            template_name = 'app1/update.html'
            context = {'form': form}
            return render(request, template_name, context)
        else:
            form = postupdateform(request.POST, instance=data)
            if form.is_valid():
                form.save()
                return redirect('register')
            context = {'form': form}
            return render(request, '/app1/update.html', context)
    except:
        return HttpResponse("please provide valid input")
