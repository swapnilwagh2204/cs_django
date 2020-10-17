from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('postComment', views.postComment, name="postComment"),
    path('', views.blogHome, name="bloghome"),
    path('<str:slug>', views.blogPost, name="blogPost"),
    path('postadd/', views.postadd, name="postadd"),

    path('delete/<int:pk>/', views.deleteview, name='delete'),
    path('update/<int:pk>/', views.updateview, name='update'),
]
