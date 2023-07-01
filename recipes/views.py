from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    text = "<h1>HOME</h1>"
    return HttpResponse(text)


def about(request):
    text = "<h1>ABOUT</h1>"
    return HttpResponse(text)


def privacy(request):
    text = "<h1>PRIVACY</h1>"
    return HttpResponse(text)