from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from quizzes.models import Theme, Answer, Question, Quiz


def index(request):
    themes = Theme.objects.all().values_list('name', flat=True)
    quizzes = Quiz.objects.all().filter(theme__name='Math')
    #quizzes = Quiz.objects.all().filter(theme__name='Math').values_list('name', flat=True)
    # allQuestions = Quiz.objects.all().values_list('questions__name', flat=True)
    # allAnswers = Question.objects.all().values_list('answers__name', flat=True)
    return render(
        request,
        'index.html',
        context={"themes": themes, "quizzes": quizzes}
    )

def quiz(request):
    themes = Theme.objects.all().values_list('name', flat=True)
    # quizzes = Quiz.objects.all().values_list('name', flat=True)
    quizzes = Quiz.objects.all()
    questions = Question.objects.all().values_list('name', flat=True)
    answers = Answer.objects.all().values_list('name', flat=True)
    return render(
        request,
        'quiz.html',
        context={"themes": themes, "quizzes": quizzes, "questions": questions, "answers": answers}
    )