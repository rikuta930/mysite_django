from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return HttpResponse("Hello, world")


def detail(request, question_id):
    return HttpResponse("u r looking at question %s." % question_id)


def result(request, question_id):
    response = "u r looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('u r voting on question %s.' % question_id)
