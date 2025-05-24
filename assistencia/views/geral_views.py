from django.http import HttpRequest
from django.shortcuts import render

def home(request:HttpRequest):
    return render(request, 'home.html')

def contato(request:HttpRequest):
    return render(request, 'contato.html')

def sobre(request:HttpRequest):
    return render(request, 'sobre.html')