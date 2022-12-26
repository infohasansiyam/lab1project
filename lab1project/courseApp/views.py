from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse("<h1>this is a first response</h1>")

def second(requst):
    return HttpResponse("this is a second response")

def third(requst):   
    return HttpResponse("this is a third response")


