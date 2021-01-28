from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from wiki.models import Term, TermRevision, TermRelated, TermPointer
import datetime
from time import time
import json

class WriteView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'wiki/write.html')

    def post(self, request, *args, **kwargs):
        term = request.POST.get('term', '')
        description = request.POST.get('description', '')
        term_related = request.POST.getlist('tagList', '')

        if term == '':
            return HttpResponse('용어를 작성해주세요.', status=400)

        term, is_created = Term.objects.get_or_create(name=term)

        if not is_created:
            return HttpResponse('이미 존재하는 용어입니다.', status=400)

        # done_check_same = []

        # for i in term_related:
        #     check_same_term = Term.objects.filter(name=i)
        #     done_check_same.append(check_same_term)

        #     if not check_same_term:
        #         not_same_term = Term.objects.get_or_create(name=i)
        #         revision_term = TermRevision.get_or_create(term_id=not_same_term.id)
        #         pointer_term = TermPointer.get_or_create(term_id=related_term.id, term_revision_id=revision_term.id)
        term_revision = TermRevision.objects.create(term_id=term.id, description=description)
        term_pointer = TermPointer.objects.create(term_id=term.id, term_revision_id=term_revision.id)

        for i in term_related:
            create_term = Term.objects.get_or_create(name=i)
            get_term_id = Term.objects.get(name=i).id
            test_term_revision = TermRevision.objects.create(term_id=get_term_id)
            test_term_pointer = TermPointer.objects.create(term_id=get_term_id, term_revision_id=test_term_revision.id)
            test_term_related = TermRelated.objects.create(term_id=get_term_id, term_revision_id=test_term_revision.id)
            term_related = TermRelated.objects.create(term_id=term.id, term_revision_id=term_revision.id, term_related_id=get_term_id)

        return redirect('/terms/{}'.format(term.id))


class DetailView(View):

    def get(self, request, *args, **kwargs):
        term = Term.objects.get(id=kwargs.get('id'))

        if not Term.DoesNotExist:
            return HttpResponse('존재하지 않는 아이디입니다', status=404)
    
        term_pointer = TermPointer.objects.get(term_id=term.id)
        term_revision = TermRevision.objects.get(id=term_pointer.term_revision_id)
        term_related = TermRelated.objects.get(term_id=term.id, term_revision_id=term_pointer.term_revision_id).term_related_id
        get_term_name = Term.objects.get(pk=term_related).name

        return render(request, 'wiki/detail.html', {
            'term': term,
            'term_item': term_revision,
            'term_related': get_term_name,
        })


class EditView(View):

    def get(self, request, *args, **kwargs):
        page_id = kwargs.get('id')
        term = Term.objects.get(id=page_id)
        term_pointer = TermPointer.objects.get(term_id=page_id).term_revision_id
        term_revision = TermRevision.objects.get(pk=term_pointer, term_id=page_id)
        term_related = TermRelated.objects.get(term_id=page_id, term_revision_id=term_revision.id)
        return render(request, 'wiki/edit.html', {
            'id': page_id,
            'term': term.name,
            'description': term_revision.description,
            'term_related': term_related.term_related
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
            'histories': revisions,
        })
    
    def post(self, request, *args, **kwargs):
        term_id = kwargs.get('id')
        post_term_revision_id = request.POST.get('return_revision', '')
        if post_term_revision_id:
            TermPointer.objects.filter(term_id=term_id).update(term_revision_id=post_term_revision_id)
        return redirect('/terms/{}'.format(term_id))


class TagView(View):

    def get(self, request, *args, **kwargs):
        text = request.GET.get('click_text')

        if request.is_ajax():
            return JsonResponse({'text': text}, status=200)

        return render(request, 'wiki/write.html')

    def post(self, request, *args, **kwargs):
        return JsonResponse({'message': "Success"}, status=200)
