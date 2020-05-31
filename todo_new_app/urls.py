from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path('', views.apiOverview, name='api'),
    path('task-list/',views.taskList, name='task-list'),
    path('task-detail/<str:pk>/',views.taskDetail, name='task-detail'),
    path('task-create/',views.taskCreate, name='task-create'),
    path('task-update/<str:pk>/',views.taskUpdate, name='task-update'),
    path('task-delete/<str:pk>/',views.taskDelete, name='task-delete'),
]
