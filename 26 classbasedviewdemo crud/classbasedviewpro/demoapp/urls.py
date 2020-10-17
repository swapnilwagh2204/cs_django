from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns =[
    path('postlist/',PostListView.as_view(),name='post-list'),
    path('postcreate/',PostCreateView.as_view(),name='post-create'),
    path('postdetail/<int:pk>/',PostDetailView.as_view(),name='post-details'),
    path('postupdate/<int:pk>/',PostUpdateView.as_view(),name='post-update'),
    path('postdelete/<int:pk>/',PostDeleteView.as_view(),name='post-delete'),
    path('login/',LoginView.as_view(template_name = 'demoapp/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout')

]