from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return HttpResponse("<h1>Wlcome To the Django web application</h1>")
def aboutpage(request):
    return HttpResponse("<h1>welcome to the aboutpage</h1>")
def contactpage(request):
    return HttpResponse("<h1>welcome to tne contact page</h1>")