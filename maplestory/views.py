from django.shortcuts import render, redirect
from wiki.models import Term, TermItem
from django.views import View

class Index(View):
    def get(self, request, *args, **kwargs):
        terms = Term.objects.all()
        return render(request, 'index.html', {
            'terms': terms,
        })
