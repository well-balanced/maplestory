from django.shortcuts import render

def index(request):
    print(1)
    return render(request, 'index.html')
