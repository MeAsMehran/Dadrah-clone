
from django.contrib import admin
from django.urls import path , include
from . import views


app_name = 'users'

urlpatterns = [
    path('signup/', views.sign_up_user, name='signupPage'),
    path('logout/', views.logout_user_and_lawyer, name='logoutPage'),
    path('login/', views.login_user, name='loginPage'),
    path('firstPage/', views.create_question_first_page, name='firstPage'),
    path('userAskedQusetion/<int:question_pk>', views.user_question, name='userAskedQuestionPage'),
    path('editUserQuestion/<int:question_pk>', views.edit_question, name='editQuestionPage'),
    path('deleteUserQuestion/<int:question_pk>', views.delete_question, name='deleteQuestion'),
    path('lawyer/signup/', views.sign_up_lawyer, name='signup_lawyer'),
    path('lawyer/login/', views.login_lawyer, name='login_lawyer'),
    # path('lawyer/logout/', views.logout_user, name='logout_lawyer'),
    path('lawyer/answer_question/<int:question_pk>', views.answer_questions, name='answerQuestion'),
    path('lawyer/edit_answer/<int:answer_pk>', views.edit_answer, name='editAnswer'),
    path('lawyer/delete_answer/<int:answer_pk>', views.delete_answer, name='deleteAnswer'),

    # path('')
    ]



