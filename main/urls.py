from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('feedback', views.feedback, name='feedback'),
    path('add_feedback', views.add_review, name='add_feedback')
]


