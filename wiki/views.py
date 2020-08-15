from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'wiki/index.html')

def detail(request, id):
    return render(request, 'wiki/detail.html')

def write(request):
    return render(request, 'wiki/write.html')

def edit(request, id):
    return render(request, 'wiki/edit.html')
