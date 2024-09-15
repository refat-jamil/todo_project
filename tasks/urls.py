from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('complete/<int:pk>/', views.task_complete, name='task_complete'),  # New URL

]
