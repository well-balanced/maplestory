from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse("테스트")
    

def testt(request, id):
    return HttpResponse("테스트22")