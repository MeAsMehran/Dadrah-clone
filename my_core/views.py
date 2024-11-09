from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect , get_object_or_404

from django.views.generic import View
from my_users.forms import QuestionForm
from . import models

# Create your views here.

## what is class based view????
# class NormalUserFunctions(View):


def welcome(request):
    latest_questions = models.Question.objects.all()
    # latest_questions = models.Question.objects.order_by('-id')[:2]

    if request.method == "GET":
        return render(request, 'welcome.html', {'questions': latest_questions})

    elif request.method == "POST":
        return redirect("users:signupPage")


def view_questions(request, question_pk):
    question = get_object_or_404(models.Question, pk=question_pk)
    answers = models.Answer.objects.filter(question_ans=question)


    if request.method == "GET":
        return render(request, 'QuestionPage.html', {'question' : question, 'answers' : answers})


@login_required
def user_dashboard(request):
    if request.method == "GET":
        return render(request, 'userDashboard.html')


@login_required
def in_person_consultation(request):

    phone_cons = get_object_or_404(models.InPersonConsultationUser, user=request.user)

    if request.method == "GET":
        return render(request, 'userDashboard/inPersonConsultation.html', {'phone_cons' : phone_cons})



@login_required
def phone_consultation(request):
    pass
















