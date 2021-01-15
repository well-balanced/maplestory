from django.db import models

class Term(models.Model):
    """ 용어 테이블 ex) Python, JavaScript ... """
    name = models.CharField(max_length=100, unique=True, verbose_name='이름')


class TermRevision(models.Model):
    """ 용어 설명 테이블 ex) Python은 귀도 반 로섬이 발표한 고급 프로그래밍 언어이다. """
    term = models.ForeignKey(Term, on_delete=models.CASCADE, verbose_name='용어')
    description = models.TextField(verbose_name='설명')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='시간')


class TermPointer(models.Model):
    """ Term과 TermRevision의 id값을 쉽게 가져오기 위한 테이블(History를 위해 만들어짐) """
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    term_revision = models.ForeignKey(TermRevision, on_delete=models.CASCADE, blank=True, default='', null=True)
    

class TermRelated(models.Model):
    """ Term에 대한 관련 용어 ex) Term이 Python 이라면 TermRelated는 Django """
    term_revision = models.ForeignKey(TermRevision, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    term_related = models.CharField(max_length=45, blank=True)
