from django.urls import path

from .views import TaskList, TaskUpdate, TaskCreate, TaskDelete

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('create', TaskCreate.as_view(), name='create'),
    path('update/<int:pk>', TaskUpdate.as_view(), name='update'),
    path('delete/<int:pk>', TaskDelete.as_view(), name='delete'),
]