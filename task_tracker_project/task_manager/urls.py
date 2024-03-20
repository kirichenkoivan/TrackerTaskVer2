from django.urls import path
from .views import task_list, create_task, edit_task, register, user_login, logout_view, delete_task

urlpatterns = [
    path('', task_list, name='login'),
    path('create/', create_task, name='create_task'),
    path('edit/<int:pk>/', edit_task, name='edit_task'),
    path('delete/<int:pk>/', delete_task, name='delete_task'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('task-list/', task_list, name='task_list'),
]
