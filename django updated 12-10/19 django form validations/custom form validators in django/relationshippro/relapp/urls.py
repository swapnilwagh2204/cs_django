from django.urls import path
from .views import empRegView,loginView

urlpatterns = [
    path('reg/',empRegView),
    path('login/',loginView),
]
