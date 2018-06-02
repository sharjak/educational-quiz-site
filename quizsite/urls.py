from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^quizzes/', include('quizzes.urls')),
    url('', views.index, name='quizsite'),
]
