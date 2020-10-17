from django.urls import path
from .views import demoView, allEmp, updateView, deleteView

urlpatterns = [
    path('index/',demoView.as_view()),
    path('allemp/', allEmp.as_view(), name='allemp'),
    path('update/<int:id>', updateView.as_view(), name='update'),
    path('delete/<int:id>', deleteView.as_view(), name='delete'),

]