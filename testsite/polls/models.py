import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    """Question Class"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """
        발행 시간이 하루 이내인지 체크하는 함수.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """Choice Class"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text