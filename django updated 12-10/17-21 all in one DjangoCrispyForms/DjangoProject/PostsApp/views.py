from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, PostsForm
from .models import registration, posts
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
            # all_posts = posts.objects.all()
            # context = {'posts':all_posts , 'current_user':usernm}
            user_posts = posts.objects.filter(author__username=usernm)
            context = {'posts': user_posts, 'current_user': usernm}
            return render(req, template_name, context)

    template_name = 'PostsApp/login.html'
    context = {}
    return render(req, template_name, context)


def UserPosts(req):
    template_name = 'PostsApp/allPosts.html'
    user_posts = posts.objects.all()
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
