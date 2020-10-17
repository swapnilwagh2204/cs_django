from django.urls import path
from .views import userCreateView,add_post,login_view,add_post1

urlpatterns = [
    path('ucreate/',userCreateView,name='user-create'),
    path('addpost/',add_post,name='add-post'),
    path('login/',login_view,name='login'),
    path('addpost1/',add_post1,name='add-post1'),
]
