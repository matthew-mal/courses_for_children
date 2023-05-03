from django.urls import path
from . import views

urlpatterns = [
    # post views
    path('', views.account, name='user'),
    path('login', views.user_login, name='login'),
    path('signup', views.signup, name='signup'),
]