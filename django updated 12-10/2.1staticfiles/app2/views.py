from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(req1):
    return HttpResponse("this is app2 view 1")

def view2(req2):
    return render(req2,'app2/view2.html')
    