
from django.contrib import admin
from django.urls import path , include
from . import views

app_name = 'core'

urlpatterns = [

    # path('', views.SiteWelcome.welcome, name='welcomePage'),
    path('question/<int:question_pk>', views.view_questions, name="viewQuestionPage"),

    ]


