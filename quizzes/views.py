from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Theme, Answer, Question, Quiz

def index(request):
    themes = Theme.objects.all().values_list('name', flat=True)
    quizzes = Quiz.objects.all().values_list('name', flat=True)
    return render(
        request,
        'index.html',
        context={"themes": themes, "quizzes": quizzes}
    )


def quiz(request):
    themes = Theme.objects.all().values_list('name', flat=True)
    quizzes = Quiz.objects.all().values_list('name', flat=True)
    questions = Question.objects.all().values_list('name', flat=True)
    answers = Answer.objects.all().values_list('name', flat=True)
    return render(
        request,
        'quiz.html',
        context={"themes": themes, "quizzes": quizzes, "questions": questions, "answers": answers}
    )