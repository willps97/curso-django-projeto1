from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('Home1')


def contato(request):
    return HttpResponse('contact')


def sobre(request):
    return HttpResponse('sobre')

