from django.urls import path
from .views import DemoView, DemoView1
urlpatterns = [
    path("index/", DemoView.as_view(), name='demo'),
    path("child/", DemoView1.as_view(), name='demo')
]
