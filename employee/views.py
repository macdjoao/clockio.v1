from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home')


def about(request):
    return HttpResponse('About')


def contact(request):
    return HttpResponse('Contact')
