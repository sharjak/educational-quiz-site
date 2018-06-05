from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='main page'),
    path('/quiz', views.quiz, name='quiz'),
]
