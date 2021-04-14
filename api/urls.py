from django.urls import path
from .views import *

urlpatterns = [
    path('', apiOverview, name="api-overview"),
    path('task-list', TaskList, name="task-list"),
    path('task-detail/<int:pk>/', TaskDetail, name="task-detail"),
    path('task-create', TaskCreate, name="task-create"),
    path('task-delete/<int:pk>', TaskDelete, name="task-delete"),
]
