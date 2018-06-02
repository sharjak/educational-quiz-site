from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.urls import path
from quizzes import views as quizzviews

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('quiz/', include('quizzes.urls')),
    path('quiz/', quizzviews.quiz),
    path('', views.index, name='quizsite')
]
