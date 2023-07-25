from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers

# Create your views here.
def index(request):
    return HttpResponse("hello worlds")
def list(request):
    test = {
        'name':'ralobo',
        'age':19,
        
    }
    #test.items()
    #return HttpResponse(test.items())
    return JsonResponse(test,safe=False)
