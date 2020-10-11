from django.urls import path
from . import views

urlpatterns=[
    path("view2/",views.view2),
    path("view21/",views.view21)
]
