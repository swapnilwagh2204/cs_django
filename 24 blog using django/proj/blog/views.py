from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment, Tag
from django.contrib import messages
from django.contrib.auth.models import User
from blog.templatetags import extras
from .forms import PostsForm, postupdateform
# Create your views here.


def blogHome(request):
    allPosts = Post.objects.all().order_by('-timeStamp')
    context = {'allPosts': allPosts}
    return render(request, "blog/blogHome.html", context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    # print(comments, replies)
    context = {'post': post, 'comments': comments,
               'user': request.user, 'replyDict': replyDict}
    return render(request, "blog/blogPost.html", context)


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(
                request, "Your comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(
                comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(
                request, "Your reply has been posted successfully")

    return redirect(f"/blog/{post.slug}")


def postadd(req):
    if req.method == "GET":
        template_name = 'blog/addpost.html'
        form = PostsForm()
        context = {'post_form': form}
        return render(req, template_name, context)

    else:
        form = PostsForm(req.POST)
        if form.is_valid():
            print("true")
            tag = form.cleaned_data['tag']
            title = form.cleaned_data['title']
            # author = form.cleaned_data['author']
            slug = form.cleaned_data['slug']
            # timestamp = form.cleaned_data['timestamp']
            content = form.cleaned_data['content']

            new_post = Post(title=title,
                            slug=slug, content=content)
            new_post.save()
            for i in tag:
                p = Tag(tag_name=i)
                p.save()
                new_post.tag.add(p)
            new_post.save()

            messages.success(req, "Your post has been posted successfully")

            return redirect('bloghome')


def deleteview(request, pk):
    try:
        data = Post.objects.get(pk=pk)
        if request.method == 'GET':
            context = {'obj': data}
            template_name = "blog/delete.html"
            return render(request, template_name, context)
        else:
            data.delete()
            return redirect('bloghome')
    except:
        return HttpResponse("please provide valid input")


def updateview(request, pk):
    try:
        data = Post.objects.get(pk=pk)
        # print(data)
        if request.method == 'GET':
            form = postupdateform(instance=data)
            # print(form)
            # print(data.pk)
            template_name = 'blog/update.html'
            context = {'form': form}
            return render(request, template_name, context)
        else:
            form = postupdateform(request.POST, instance=data)
            if form.is_valid():
                # print("true")
                form.save()
                return redirect('bloghome')
            context = {'form': form}
            return render(request, 'blog/update.html', context)
    except:
        return HttpResponse("please provide valid input")
