from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('add/', views.add_article, name='add_article'),
    path('<int:pk>', views.NewsAddress.as_view(), name='news_detail')
]


