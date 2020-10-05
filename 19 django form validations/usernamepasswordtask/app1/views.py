from django.shortcuts import render,HttpResponse
from . import views
from . models import emp
from .forms import empform
# Create your views here.
def empview(req5):
    if req5.method=='GET':
        print("get request received")
        request=req5
        emp1=empform()
    else:
        print("post request received")
        emp1=empform(req5.POST)
        if emp1.is_valid():
            print("form is valid")
            un=emp1.cleaned_data['username']
            ps=emp1.cleaned_data['password']
            s1=emp(username=un,password=ps)
            s1.save()
            return HttpResponse(" record entered")
    context ={'st':emp1}
    template_name="app1/form.html"
    return render(req5, template_name, context)
    

