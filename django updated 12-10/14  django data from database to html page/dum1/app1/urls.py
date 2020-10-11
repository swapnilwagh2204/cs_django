from django.urls import path
from . import views

urlpatterns=[
    path("ss/",views.view1),
    path('postt/',views.view2)
]
