from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("student/", views.view1),
    path("post/", views.view2),
]
