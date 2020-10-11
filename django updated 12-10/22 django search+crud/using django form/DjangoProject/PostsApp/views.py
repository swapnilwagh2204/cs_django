from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, PostsForm, postupdateform
from .models import registration, posts
from django.db.models import Q
# Create your views here.


def regView(req):
    if req.method == 'GET':
        form = UserForm()
    else:
        form = UserForm(req.POST)
        if form.is_valid():
            n = form.cleaned_data['Name']
            e = form.cleaned_data['Email']
            g = form.cleaned_data['Gender']
            un = form.cleaned_data['Username']
            pas = form.cleaned_data['Password']
            entry = registration(name=n, email=e, gender=g,
                                 username=un, password=pas)
            entry.save()
            return redirect('Userlogin')
    template_name = 'PostsApp/registration.html'
    context = {'form': form, }
    return render(req, template_name, context)


def loginView(req):
    if req.method == 'POST':
        usernm = req.POST['un']
        pswd = req.POST['pas']
        user = registration.objects.filter(username=usernm, password=pswd)
        if user:
            template_name = 'PostsApp/userPosts.html'
            # all_posts = posts.objects.all().order_by('-date')
            # context = {'posts': all_posts, 'current_user': usernm}
            user_posts = posts.objects.filter(
                author__username=usernm).order_by('-date')
            context = {'posts': user_posts, 'current_user': usernm}
            return render(req, template_name, context)

    template_name = 'PostsApp/login.html'
    context = {}
    return render(req, template_name, context)


def UserPosts(req):
    template_name = 'PostsApp/allPosts.html'
    user_posts = posts.objects.all().order_by('-date')
    context = {'posts': user_posts}
    return render(req, template_name, context)


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
            return redirect('final')


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
        # print(pk)
        data = posts.objects.get(pk=pk)
        # print(data.pk)
        if request.method == 'GET':
            form = postupdateform(
                initial={'Content': data.content, 'Title': data.title})
            print(form)
            template_name = 'PostsApp/update.html'
            context = {'form': form}
            return render(request, template_name, context)
        else:
            form = postupdateform(request.POST)
            print(form)
            if form.is_valid():
                data.content = form.cleaned_data.get('Content')
                # data.author = form.cleaned_data('author')
                data.title = form.cleaned_data.get('Title')
                print(data.content)
                print(data.title)
                data.save()
                return redirect('UserPosts')
            context = {'form': form}
            return render(request, '/PostsApp/update.html', context)
    except:
        return HttpResponse("please provide valid input")
