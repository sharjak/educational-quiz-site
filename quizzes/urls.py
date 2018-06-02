from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('/index', views.index, name='mainpage'),
    path('/quiz', views.quiz, name='quiz'),
    path('/ha', views.quiz)
]
