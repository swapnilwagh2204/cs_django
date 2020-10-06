from django.shortcuts import render
from django.http import HttpResponse
from . forms import regForm,postuserform
from .models import Users,postt
from . import views

def empRegView(request):
    template_name = 'app1/register.html'

    if request.method == 'GET':
        form = regForm()
        return render(request,template_name,{'form':form})
    else:
        form = regForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data.get('username')
            p = form.cleaned_data.get('password')
            fn = form.cleaned_data.get('fullname')
            ad = form.cleaned_data.get('address')
            g = form.cleaned_data.get('gender')

            emp = Users(Username=u,Password=p,Fullname=fn,Address=ad,Gender=g)
            emp.save()
            return render(request,'app1/login.html')
        return render(request,template_name,{'form':form})



def loginview(request):
    if request.method == 'GET':
        template_name = "app1/login.html"
        return render(request, template_name)
    else:
        u = request.POST['username']
        p = request.POST['password']
        if Users.objects.get(Username=u,Password=p):
            
            posts= postt.objects.filter(overview__Username=u)
            # Tweets.objects.(user=current_user
            context = {"us": posts}
            return render(request,"app1/display.html",context)
        return render(request,"app1/login.html")

# def userposts(req6):
#     if req6.method=='GET':
#         print("get request received")
#         request=req6
#         pst=postuserform()
#         context ={'st':pst}
#         template_name="app1/formpost.html"
#         return render(request, template_name, context)
#     else:
#         print("post request received")
#         con=req6.POST['content']
#         print(con)
#         crtb=req6.POST['created_by']
#         print(crtb)
#         s1=postt(content=con,created_by=crtb)
#         s1.save()
#         return HttpResponse(" record entered")


'''
def userposts(request):
    if request.method=='GET':
        print("get method received")
        form=postuserform()
    else:
        print("post method received")
        form=postuserform(request.POST)
        if form.is_valid():
            form.save()
            print("data inserted,redirecting to dispstudent")
            # return redirect('displa')
    template_name='app1/addstudent.html'
    context={'form':form}
    return render(request, template_name,context)

def disstu(request):
    obj=User
    .objects.filter(Username)
    template_name='app1/dispstudent.html'
    context={'students':obj}
    return render(request, template_name, context)
'''