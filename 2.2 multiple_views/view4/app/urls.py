from django.urls import path

from django.urls import  path
from . import views
urlpatterns = [
    path("view1/",views.view1),

    path("view2/", views.view2),
    path("view3/",views.view3),
    path("view4/",views.view4),
]
