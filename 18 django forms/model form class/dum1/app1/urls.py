
from django.urls import path
from . import views

urlpatterns = [
    path("form/", views.emp),
    path("formpost/", views.pstusr),
    path("dispstu/", views.disstu),
    path("disppost/", views.dispost),
]
