from app1.views import insertpost
from django.urls import path
from . import views

urlpatterns=[
    path("student/",views.view1),
    path('postt/',views.view2),
    path('studentinsert/',views.insertdata),
    path("postinsert/",views.insertpost)
]
