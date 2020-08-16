from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from wiki.models import Term, TermItem
import datetime

class Write(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'wiki/write.html')

    def post(self, request, *args, **kwargs):
        term = request.POST.get('term')
        description = request.POST.get('description', '')

        if not term and not description:
            return HttpResponse('용어와 설명을 꼭 작성해주세요.', status=400)

        term, is_created = Term.objects.get_or_create(name=term)

        if not is_created:
            return HttpResponse('이미 존재하는 용어입니다.', status=400)

        term = TermItem.objects.create(term=term, description=description)
        return redirect('/terms/{}'.format(term.pk))

class Detail(View):
    def get(self, request, *args, **kwargs):
        # print(kwargs.get('id'))
        return render(request, 'wiki/detail.html')

class Edit(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'wiki/edit.html')

    def post(self, request, *args, **kwargs):
        print(args, kwargs)
        return render(request, 'wiki/detail.html')
