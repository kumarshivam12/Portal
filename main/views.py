from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("wow this is <strong>awesone benchod</strong>")
