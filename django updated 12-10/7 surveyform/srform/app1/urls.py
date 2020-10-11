from django.urls import path
from . import views
urlpatterns = [
    path("app1/",views.view1)
]
