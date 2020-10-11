from django.urls import path

from . import views

urlpatterns = [

    path('reg/', views.empRegView, name='register'),
    # path('formpost/',views.userposts,name='postform'),
    path('log/', views.loginview),
    path('delete/<int:pk>/', views.deleteview, name='delete'),
    path('update/<int:pk>/', views.updateview, name='update'),


]
