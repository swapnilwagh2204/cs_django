from django.urls import path

from . import views

urlpatterns = [

    path('reg/',views.empRegView),
    # path('formpost/',views.userposts,name='postform'),
    path('log/',views.loginview),
]
