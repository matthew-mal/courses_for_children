from django.urls import path, include
from . import views

urlpatterns = [
    # post views
    path('', views.user_login, name='login'),
]