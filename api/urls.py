from django.urls import path
from .views import *

urlpatterns = [
    path('', apiOverview, name="api-overview"),
    path('task-list', TaskList, name="task-list"),
    path('task-detail/<slug:slug>/', TaskDetail, name="task-detail"),
    path('task-create', TaskCreate, name="task-create"),
]
