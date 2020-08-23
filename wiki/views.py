from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from wiki.models import Term, TermRevision, TermRelated
import datetime

class WriteView(View):

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

        term = TermRevision.objects.create(term=term, description=description)
        return redirect('/terms/{}'.format(term.term_id))

class DetailView(View):

    def get(self, request, *args, **kwargs):
        try:
            term = Term.objects.get(id=kwargs.get('id'))
        except Term.DoesNotExist:
            return HttpResponse('존재하지 않는 아이디입니다.', status=404)

        term_item = TermRevision.objects.filter(term=term).order_by('-created_at').first()
        return render(request, 'wiki/detail.html', {
            'term': term,
            'term_item': term_item,
        })

class EditView(View):

    def get(self, request, *args, **kwargs):
        page_id = (kwargs.get('id'))
        get_term = Term.objects.get(id=page_id).name
        get_description = TermRevision.objects.filter(term_id=page_id).order_by('-created_at').first().description
        return render(request, 'wiki/edit.html', {
            'id': page_id,
            'term': get_term,
            'description': get_description,
        })

    def post(self, request, *args, **kwargs):
        page_id = (kwargs.get('id'))
        description = request.POST.get('description', '')
        TermRevision.objects.create(description=description, term_id=page_id)
        return redirect('/terms/{}'.format(page_id))

class HistoryView(View):

    def get(self, request, *args, **kwargs):
        try:
            term = Term.objects.get(id=kwargs.get('id'))
        except Term.DoesNotExist:
            return HttpResponse('존재하지 않는 아이디입니다.', status=404)

        history = TermRevision.objects.filter(term=term).order_by('-created_at')
        return render(request, 'wiki/history.html', {
            'term': term,
            'history': history,
        })