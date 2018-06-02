from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def quiz(request):
    template = loader.get_template('quiz.html')
    return HttpResponse(template.render({}, request))