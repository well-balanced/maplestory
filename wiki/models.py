from django.db import models

# user(미리 GitHub 연동 작업까지 생각), title, content, hits(조회수), Revision, comment, Like or Dislike
class Term(models.Model):
    user = models.CharField(max_length=20)
    term_title = models.TextField()
    term_content = models.TextField()
    # hits = 

class Comment(models.Model):
    comment_date = models.DateField(auto_now_add=True)
    comment_content = models.CharField(max_length=200)
    # comment_writer = 