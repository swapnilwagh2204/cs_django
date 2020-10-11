from django.urls import path

from . import views

urlpatterns = [

    path('reg/',views.registerview),
    path('log/',views.loginview),
]
