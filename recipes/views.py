from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html')


def sobre(request):
    return HttpResponse('Uma linda STRING 2222222 ')

