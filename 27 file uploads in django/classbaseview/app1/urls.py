from django.urls import path

from .views import homeview, deleteview, updateview, loginview, Emplist, Empcreate, Empupdate, Empdelete, Postimg

urlpatterns = [
    path('home/',homeview.as_view(),name = 'home'),
     path('update/<int:pk>/',updateview.as_view(),name = 'update'),
    path('delete/<int:pk>/',deleteview.as_view(),name = 'delete'),
    path('login/',loginview.as_view(),name = 'log'),
    path('ae/',Emplist.as_view(),name = 'all Employs'),
    path('create/',Empcreate.as_view(),name = 'create'),
    path('updte/<int:pk>/',Empupdate.as_view(),name = 'updte'),
    path('delte/<int:pk>/',Empdelete.as_view(),name = 'delte'),
    path('post',Postimg.as_view(),name = 'imgpost'),

]