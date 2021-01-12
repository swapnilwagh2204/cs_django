from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.regView, name='UserRegister'),
    path('login/', views.loginView, name='Userlogin'),
    path('logout/', views.logoutview, name='Userlogout'),
    path('addpost/', views.postView, name='AddPost'),
    path('allposts/', views.UserPosts, name='UserPosts'),
    path('final/', views.finalView, name='final'),
    path('search/', views.search, name="search"),
    path('delete/<int:pk>/', views.deleteview, name='delete'),
    path('update/<int:pk>/', views.updateview, name='update'),

]
