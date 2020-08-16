from django.db import models

# user(미리 GitHub 연동 작업까지 생각), title, content, hits(조회수), Revision, comment, Like or Dislike
class Term(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='이름')

class TermItem(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE, verbose_name='용어')
    description = models.TextField(null=True, blank=True, verbose_name='설명')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='시간')