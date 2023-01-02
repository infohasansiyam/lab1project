from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def first(request):
    return render(request,'index.html')

def second(requst):
    return render("this is a second response")

def third(requst):   
    return render("this is a third response")


