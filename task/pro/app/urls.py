from django.urls import path
from . import views

urlpatterns=[
    path("fa1/",views.fun1),
    path("fa2/",views.fun2)
]
