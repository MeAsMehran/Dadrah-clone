
from django.contrib import admin
from django.urls import path , include
from . import views as userView
from my_core import views as coreView


app_name = 'users'

urlpatterns = [
    path('signup/', userView.sign_up_user, name='signupPage'),
    path('logout/', userView.logout_user_and_lawyer, name='logoutPage'),
    path('login/', userView.login_user, name='loginPage'),
    path('firstPage/', userView.create_question_first_page, name='firstPage'),
    path('userAskedQusetion/<int:question_pk>', userView.user_question, name='userAskedQuestionPage'),
    path('editUserQuestion/<int:question_pk>', userView.edit_question, name='editQuestionPage'),
    path('deleteUserQuestion/<int:question_pk>', userView.delete_question, name='deleteQuestion'),
    path("rate_answer/<int:answer_pk>/", userView.rate_answer, name="rate_answer"),
    path('dashboard/', coreView.user_dashboard, name='dashboard'),

    path('dashboard/inPersonConsultation', coreView.in_person_consultation, name='inPersonCon'),
    path('dashboard/phoneConsultation', coreView.phone_consultation, name='phoneCon'),





    path('lawyer/signup/', userView.sign_up_lawyer, name='signup_lawyer'),
    path('lawyer/login/', userView.login_lawyer, name='login_lawyer'),
    # path('lawyer/logout/', views.logout_user, name='logout_lawyer'),
    path('lawyer/answer_question/<int:question_pk>', userView.answer_questions, name='answerQuestion'),
    path('lawyer/edit_answer/<int:answer_pk>', userView.edit_answer, name='editAnswer'),
    path('lawyer/delete_answer/<int:answer_pk>', userView.delete_answer, name='deleteAnswer'),





    # path('')
    ]



