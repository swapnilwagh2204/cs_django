from django.http import HttpResponse

def view1(request):
    return HttpResponse("this is first django project")

def view2(request):
    return HttpResponse("this is second django project")