from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.


def ping(request):
    data = {'Hello ': 'pong!'}
    return JsonResponse(data)


def index(request):
    context = 'Hello Word, My name Roman, ist my test-sertver-on-heroku'
    return JsonResponse(context)
