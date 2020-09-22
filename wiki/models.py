from django.db import models

class Term(models.Model): # 용어 저장 테이블
    name = models.CharField(max_length=100, unique=True, verbose_name='이름')

class TermRevision(models.Model): # 용어에 대한 설명 테이블
    term = models.ForeignKey(Term, on_delete=models.CASCADE, verbose_name='용어')
    description = models.TextField(verbose_name='설명')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='시간')

class TermPointer(models.Model): # Revision 롤백 기능을 위한 테이블
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    term_revision = models.ForeignKey(TermRevision, on_delete=models.CASCADE, blank=True, default='', null=True)

class TermRelated(models.Model): # 관련 Term 테이블
    term_revision = models.ForeignKey(TermRevision, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
