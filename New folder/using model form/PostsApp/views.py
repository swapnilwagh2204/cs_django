from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, PostsForm, postupdateform
from .models import registration, posts
from django.db.models import Q
# Create your views here.


def regView(request):
    if request.method == 'GET':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Userlogin')
    template_name = 'PostsApp/registration.html'
    context = {'form': form}
    return render(request, template_name, context)


def loginView(request):
    if request.method == 'GET':
        template_name = 'PostsApp/login.html'
        context = {}
        return render(request, template_name, context)
    else:
        u = request.POST['un']
        p = request.POST['pas']
        print(u, p)
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('UserPosts')
        else:
            return HttpResponse("invalid credentials")


def logoutview(request):
    logout(request)
    return redirect('Userlogin')


@login_required(login_url='Userlogin')
def UserPosts(req):
    template_name = 'PostsApp/allPosts.html'
    user_posts = posts.objects.all().order_by('-date')
    context = {'posts': user_posts}
    return render(req, template_name, context)


@login_required(login_url='Userlogin')
def postView(req):
    if req.method == 'GET':
        template_name = 'PostsApp/addPost.html'
        form = PostsForm()
        context = {'post_form': form}
        return render(req, template_name, context)
    else:
        form = PostsForm(req.POST)
        if form.is_valid():
            auth = form.cleaned_data['Author']
            title = form.cleaned_data['Title']
            content = form.cleaned_data['Content']
            # date = form.cleaned_data['Date']
            new_post = posts(author=auth, title=title, content=content)
            new_post.save()
            return redirect('AddPost')


def finalView(req):
    template_name = 'PostsApp/final.html'
    context = {'msg': 'Post Added Successfully'}
    return render(req, template_name, context)


def search(request):
    query = request.GET['query']
    titlePosts = posts.objects.filter(
        Q(title__icontains=query) | Q(author__username__icontains=query) | Q(content__icontains=query)).order_by('-date')
    # contentposts = posts.objects.filter(content__icontains=query)
    # authorposts = posts.objects.filter(author__icontains=query)
    # allPosts = posts.objects.all()
    params = {'allPosts': titlePosts}
    return render(request, 'PostsApp/search.html', params)
    # return HttpResponse("this is search")


def deleteview(request, pk):
    try:
        data = posts.objects.get(pk=pk)
        if request.method == 'GET':
            context = {'obj': data}
            template_name = "PostsApp/delete.html"
            return render(request, template_name, context)
        else:
            data.delete()
            return redirect('register')
    except:
        return HttpResponse("please provide valid input")


def updateview(request, pk):
    try:
        data = posts.objects.get(pk=pk)
        if request.method == 'GET':
            form = postupdateform(instance=data)
            template_name = 'PostsApp/update.html'
            context = {'form': form}
            return render(request, template_name, context)
        else:
            form = postupdateform(request.POST, instance=data)
            if form.is_valid():
                # print("true")
                form.save()
                return redirect('UserPosts')
            context = {'form': form}
            return render(request, '/PostsApp/update.html', context)
    except:
        return HttpResponse("please provide valid input")
