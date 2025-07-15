from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('complete/<str:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<str:task_id>/', views.delete_task, name='delete_task'),
]
