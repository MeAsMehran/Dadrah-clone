from django.db import models

class Question(models.Model):
    question_title = models.CharField(max_length=64)
    question_text = models.TextField()
    question_date = models.DateTimeField()
    question_url = models.CharField(max_length=64)

class Answer(models.Model):
    answer_text = models.TextField()
    answer_date = models.DateTimeField()
    answer_lawyer = models.CharField(max_length=64)
    answer_rate = models.FloatField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')


