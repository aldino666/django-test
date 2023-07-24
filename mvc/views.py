from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers

# Create your views here.
def index(request):
    return HttpResponse("bonjour tout le mondesdfsdfdsf")
def list(request):
    test = [1,2,1,2,5]
    return JsonResponse(test,safe=False)
