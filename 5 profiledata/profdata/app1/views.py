from django.shortcuts import render
from django.http import request

# Create your views here.


class student:
    def __init__(self, rn, nm, marks):
        self.rn = rn
        self.nm = nm
        self.marks = marks

    def __str__(self):
        return "{},{},{}".format(self.rn, self.nm, self.marks)


s1 = student(1, 'swapnil', 100)
s2 = student(2, 'sss', 200)
s3 = student(3, 'waaa', 300)


def dct(req2):
    context = {'ss': [s1], 'ss1': [s2], 'ss2': [s3]}
    request = req2
    template_name = 'app1/index.html'

    return render(request, template_name, {'ls':context})


def view1(req1):
    return render(req1, "app1/index.html")
