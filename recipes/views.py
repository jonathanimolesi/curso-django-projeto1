from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse('Home Sweet Home!')


def sobre(request):
    return HttpResponse('Uma linda STRING 2222222 ')

