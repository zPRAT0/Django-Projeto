from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    lista = [i for i in range(1, 10)]
    return render(request, 'recipes/home.html', {'name': lista})


def about(request):
    text = "<h1>ABOUT</h1>"
    return render(request, 'me-apague/temp.html')


def privacy(request):
    text = "<h1>PRIVACY</h1>"
    return HttpResponse(text)
