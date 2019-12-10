from django.db import models
from django.contrib import admin


class Questions(models.Model):
    question_title = models.TextField(max_length=30, null=False)
    question_text = models.TextField(null=False)
    published_date = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.question_title


class Comments(models.Model):
    question = models.ForeignKey(
        Questions, on_delete=models.SET_NULL, null=True)
    author = models.CharField(max_length=30,)
    comment_text = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text
