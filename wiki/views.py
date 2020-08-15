from django.shortcuts import render

# Create your views here.

def write(request):
    return render(request, 'write.html')

def detail(request, id):
    return render(request, 'term.html')

def 