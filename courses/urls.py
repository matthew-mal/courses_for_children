from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_courses, name='courses'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('<int:course_id>/tasks/', views.task_list, name='tasks'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('<int:course_id>/tasks/add/', views.add_task, name='add_task'),
    path('<int:pk>/tasks/update', views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('add', views.add_course, name='add_course'),
]


