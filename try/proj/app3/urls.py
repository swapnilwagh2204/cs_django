
from django.urls import path
from . import views
urlpatterns = [
    path("index/", views.index),
    path("info/", views.info),
    path("msg/", views.msg),
]
