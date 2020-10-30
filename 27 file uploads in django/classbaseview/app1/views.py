from django import views
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Student, Employee, Post


# Class Based Views .


class homeview(views.View):

    template_name = 'app1/home.html'
    students = Student.objects.all()
    context = {'students':students}

    def get(self,request):

        students = Student.objects.all()
        context = {'students': students}

        return render(request,self.template_name,context)

    def post(self,request):
        r=request.POST['rollno']
        n=request.POST['name']
        m=request.POST['marks']
        sobj=Student(rollno=r,name=n,marks=m)
        sobj.save()
        students = Student.objects.all()
        context = {'students': students}
        return render(request, self.template_name, context)


class deleteview(views.View):

    def get(self,request,**kwargs):
        pk=kwargs['pk']
        sobj=Student.objects.get(pk=pk)
        sobj.delete()
        return redirect('home')

        # students=Student.objects.all()
        # context  = {'students':students}
        # # return render(request,'app1/home.html',context)




class updateview(views.View):

    def get(self,request,**kwargs):
        pk=kwargs['pk']
        obj=Student.objects.get(pk=pk)
        context = {'obj':obj}
        return render(request,'app1/update.html',context)

    def post(self,request,**kwargs):
        pk=kwargs['pk']
        obj=Student.objects.get(pk=pk)
        obj.rollno=request.POST['rollno']
        obj.name=request.POST['name']
        obj.marks=request.POST['marks']
        obj.save()
        return redirect('home')

        # students = Student.objects.all()
        # context ={'students':students}
        # # return render(request,'app1/home.html',context)



class loginview(views.View):

    def get(self,request):
        return render(request,'app1/login.html')

    def post(self,request):

        user=request.POST['username']
        passd=request.POST['password']
        user=authenticate(username=user,password=passd)
        print(user)
        if user:
            login(request,user)
            return HttpResponse('authenticate successfully')
        return render(request,'app1/login.html')




# Class Based Generic Views .


class Emplist(ListView):

    # model = Employee

    queryset = Employee.objects.all()

# Get context data is used to set context .
    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data()

        context['data'] = '***********| Employee Model Data |************'

        return context

# get queryset is used to get what data we want to send to html page.
    # i.e. filtering/ordering data .

    def get_queryset(self):

        qs = super(Emplist,self).get_queryset()

        #qs = qs.filter(username = 'rushi')  # To seeing only particular objects from model.

        return qs





class Empcreate(CreateView) :

    model = Employee

    fields = ['name','username','password']

    success_url = '/ap/ae/'


class Empupdate(UpdateView) :
    model = Employee

    fields = ['name','username','password']



    success_url = '/ap/ae/'

class Empdelete(DeleteView) :

    model = Employee

    template_name = 'app1/employee_delete.html'

    success_url = '/ap/ae/'



class Postimg(ListView) :

    model = Post

    template_name = 'app1/post.html'

