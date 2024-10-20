from django.shortcuts import render

from django.views.generic import View
from my_users.forms import QuestionForm
from . import models

# Create your views here.

## what is class based view????
# class NormalUserFunctions(View):


def welcome(request):

    # latest_questions = models.Question.objects.all()
    latest_questions = models.Question.objects.order_by('-id')[:2]

    return render(request, 'welcome.html', {'questions' : latest_questions})

def signup_user(request):
    pass











