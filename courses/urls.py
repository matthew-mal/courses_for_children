from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_courses, name='courses'),
]


