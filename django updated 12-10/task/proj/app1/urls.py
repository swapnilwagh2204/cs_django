from django.urls import path
from . import views
urlpatterns = [
    path("home/",views.view1),
    path("about/",views.view2),
    path("contact/",views.view3),
    path("info/",views.view4),

]
