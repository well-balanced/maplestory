from django.db import models

class Term(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='이름')

class TermRevision(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE, verbose_name='용어')
    description = models.TextField(verbose_name='설명')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='시간')

class TermRelated(models.Model):
    term_revision = models.ForeignKey(TermRevision, on_delete=models.CASCADE,)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)