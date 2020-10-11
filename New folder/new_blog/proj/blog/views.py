from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, "blog/blogHome.html", context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(
        post=post).exclude(parent=None)  # parent=not none
    # print(comments, replies)
    rd = {}
    for rep in replies:
        if rep.sno not in rd.keys():
            rd[rep.sno] = [rep]
        else:
            rd[rep.sno].append(rep)
    # print(comments, replies)
    # print(rd)
    context = {'post': post, 'comments': comments, 'replydict': rd}
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
