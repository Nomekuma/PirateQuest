from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")
    
