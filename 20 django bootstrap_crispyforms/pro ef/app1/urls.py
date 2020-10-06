from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.home),
    path("about/",views.about),
    path("contact/",views.contact),
    path("info/",views.info,name="info"),
    path('addstudent/',views.addstu,name="addstu"),
    path('dispstudent/',views.disstu,name="disstu"),
]
