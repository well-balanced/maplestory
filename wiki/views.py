from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from wiki.models import Term, TermRevision, TermRelated, TermPointer
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
        term_revision = TermRevision.objects.create(term=term, description=description)
        test = TermPointer.objects.create(term_id=term.id, term_revision_id=term_revision.id)
        return redirect('/terms/{}'.format(term.id))

class DetailView(View):

    def get(self, request, *args, **kwargs):
        try:
            term = Term.objects.get(id=kwargs.get('id'))
        except Term.DoesNotExist:
            return HttpResponse('존재하지 않는 아이디입니다.', status=404)
        term_pointer = TermPointer.objects.filter(term_id=term.id).get()
        term_revision = TermRevision.objects.filter(id=term_pointer.term_revision_id).get()
        return render(request, 'wiki/detail.html', {
            'term': term,
            'term_item': term_revision,
        })

class EditView(View):

    def get(self, request, *args, **kwargs):
        page_id = kwargs.get('id')
        term_name = Term.objects.get(id=page_id).name
        term_pointer = TermPointer.objects.filter(term_id=page_id).get().term_revision_id
        description = TermRevision.objects.filter(term_id=page_id).get(pk=term_pointer).description
        return render(request, 'wiki/edit.html', {
            'id': page_id,
            'term': term_name,
            'description': description,
        })

    def post(self, request, *args, **kwargs):
        page_id = kwargs.get('id')
        description = request.POST.get('description', '')
        term_revision = TermRevision.objects.create(description=description, term_id=page_id)
        TermPointer.objects.filter(term_id=page_id).update(term_revision_id=term_revision.id)
        return redirect('/terms/{}'.format(page_id))

class HistoryView(View):

    def get(self, request, *args, **kwargs):
        try:
            term = Term.objects.get(id=kwargs.get('id'))
        except Term.DoesNotExist:
            return HttpResponse('존재하지 않는 아이디입니다.', status=404)
        revisions = TermRevision.objects.filter(term=term).order_by('-created_at')
        return render(request, 'wiki/history.html', {
            'term': term,
            'history': revisions,
            'id': term.id,
        })
    
    def post(self, request, *args, **kwargs):
        term_id = kwargs.get('id')
        post_term_revision_id = request.POST.get('return_revision', '')
        if post_term_revision_id:
            TermPointer.objects.filter(term_id=term_id).update(term_revision_id=post_term_revision_id)
        return redirect('/terms/{}'.format(term_id))
