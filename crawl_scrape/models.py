from django.db import models

# Create your models here.



class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_title = models.CharField(max_length=256, blank=False)
    created_at = models.DateField(auto_now=True)
    question_text = models.TextField(blank=False)
    question_url = models.CharField(max_length=64, blank=False)


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    answer_content = models.TextField(blank=False)
    created_at = models.DateField(auto_now=True)
    answer_lawyer = models.CharField(max_length=64)
    answer_rate = models.FloatField(blank=False, default=0)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)










