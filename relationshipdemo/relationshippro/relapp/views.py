from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.




def userCreateView(request):
    form = MyUserCreationForm()
    if request.method=='GET':
        template_name = 'relapp/ucreate.html'
        return render(request,template_name,{'form':form})
    else:
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User Created SuccessFully')
        return render(request,'relapp/ucreate.html',{'form':form})


@login_required(login_url='/relapp/login/')
def add_post(request):
    form = PostModelForm()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            tag = form.cleaned_data.get('tag')
            title = form.cleaned_data.get('title','')
            content = form.cleaned_data.get('content')
            user = request.user
            #p = Post(title=title,content=content,created_by=user)
            #p.save()
            p = Post.objects.create(title=title,content=content,created_by=user)
            tags = tag.split()
            for tg in tags:
                tg = tg.lower()
                #t, tc = Tag.objects.get_or_create(tag_name=tg)
                try:
                    t = Tag.objects.get(tag_name=tg)
                    p.tag.add(t)
                except:
                    tc = Tag.objects.create(tag_name=tg)
                    p.tag.add(tc)
                p.save()
            return HttpResponse('Post Created by user',user.username)
        return render(request,'relapp/addpost.html',{'form':form})
    return render(request,'relapp/addpost.html',{'form':form})


@login_required(login_url='/relapp/login/')
def add_post1(request):
    form = PostModelForm1()
    if request.method == 'POST':
        form = PostModelForm1(request.POST)
        if form.is_valid():
            form.save()
            user = request.user
            return HttpResponse('Post Created by user',user.username)
        return render(request,'relapp/addpost.html',{'form':form})
    return render(request,'relapp/addpost.html',{'form':form})


def login_view(request):
    print(request.GET)
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user :
            login(request,user)
            next = request.POST.get('a')
            if next:
                print(request.POST.get('next'))
                return redirect(request.POST.get('next'))
            return redirect('user-create')
        return render(request,'relapp/login.html')
    return render(request, 'relapp/login.html')

