from django.shortcuts import render

from .models import Users


def registerview(request):
    if request.method == 'GET':
        template_name = "app1/register.html"
        return render(request, template_name)
    else:
        u = request.POST['un']
        p = request.POST['pw']
        fn = request.POST['nm']
        e = request.POST['em']
        a = request.POST['adr']
        g = request.POST['Gender']
        if u and p and fn and e and a and g:
            u1 = Users(Username=u, Password=p, Fullname=fn,
                       Email=e, Address=a, Gender=g)
            u1.save()
            return render(request, "app1/login.html")
        return render(request, "app1/register.html")


def loginview(request):
    if request.method == 'GET':
        template_name = "app1/login.html"
        return render(request, template_name)
    else:
        u = request.POST['un']
        p = request.POST['pw']
        if Users.objects.get(Username=u) and Users.objects.get(Password=p):
            user = Users.objects.all()
            context = {"Users": user}
            return render(request, "app1/display.html", context)
        return render(request, "app1/login.html")
