
from django.urls import path
from . import views

urlpatterns = [
    path("form/", views.emp),
    path("formpost/", views.pstusr),
    path("studentdisplay/", views.stu_dis),
    path("postdisp/", views.pstdis),
]
