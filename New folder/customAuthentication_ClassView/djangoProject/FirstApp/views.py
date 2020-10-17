from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import views
from .forms import EmpForm
from .models import Employee
# Create your views here.

class demoView(views.View):
    template_name = 'FirstApp/index.html'
    context = {}
    def get(self,request):
        self.context['form'] = EmpForm()
        return render(request,self.template_name,self.context)

    def post(self,request):
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('allemp')

class allEmp(views.View):
    template_name = 'FirstApp/allemp.html'
    context = {}
    def get(self,request):
        self.context['data'] = Employee.objects.all()
        return render(request, self.template_name, self.context)


class updateView(views.View):
    template_name = 'FirstApp/update.html'
    context = {}
    def get(self,request, id):
        try:
            obj = Employee.objects.get(id=id)
            form = EmpForm(instance=obj)
            self.context['form'] = form
            return render(request, self.template_name,self.context)
        except:
            return HttpResponse('Record not found')
    def post(self, request, id):
        print('in post method')
        obj = Employee.objects.get(id=id)
        form = EmpForm(request.POST, instance=obj)
        if form.is_valid():
            print('form is valid')
            form.save()
        return redirect('allemp')

class deleteView(views.View):
    context = {}
    template_name = 'FirstApp/delete_confirm.html'
    def get(self,request,id):
        try:
            obj = Employee.objects.get(id=id)
            self.context['obj'] = obj
            return render(request, self.template_name, self.context)
        except:
            return HttpResponse('enter valid data')

    def post(self, request, id):
        obj = Employee.objects.get(id=id)
        obj.delete()
        return redirect('allemp')






