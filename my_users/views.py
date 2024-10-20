
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from .models import NormalUser
from django.http import JsonResponse
from django.contrib.auth import login , logout , authenticate
import random , string
# from twilio.rest import Client
# from . import keys
from django.contrib.auth.models import User
# from flask import Flask, jsonify
from django.views.decorators.csrf import csrf_exempt
import json
from my_core import models
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required
from .forms import SignupLawyerForm

# Create your views here.



# def signup_login_user(request):
#     """this method is for signing up a new user or loging in an existed user"""
#     if request.method == 'GET':
#         return render(request, 'signup_user.html')
#
#     elif request.method == 'POST':
#         new_phone_number = request.POST['phoneNumberInput']
#         ver_code = generate_code()
#
#         client = Client(keys.account_sid, keys.auth_token)
#         message = client.messages.create(
#             body=f"Your verification code is: {ver_code}",
#             from_=keys.twilio_number,
#             to=keys.my_phone_number)
#
#
#         if NormalUser.objects.filter(phone=new_phone_number).exists():      # The new phone number exists in the database. So the user login if the ver_code is as same as the verification code which is entered
#             if request.POST['verificationCode'] == ver_code:
#                 new_user = authenticate(request, phone=new_phone_number)
#                 login(request, new_user)
#                 return redirect('welcomePage')
#             else:
#                 return render(request, 'signup_user.html', {'error': 'The verification codes do not match'})
#             # return JsonResponse({'status': 'exists', 'message':'Phone number is available!'})
#
#         else:
#             if request.POST['verificationCode'] == ver_code:
#                 new_user = NormalUser.objects.create(phone=new_phone_number)    # The new phone number doesn't exist in the database. So we create a normalUser with that phone number if the ver_code and verification code is same
#                 new_user.save()
#                 login(request, new_user)
#                 return redirect('welcomePage')
#             else:
#                 return render(request, 'signup_user.html', {'error': 'The verification codes do not match'})



def sign_up_user(request):
    if request.method == 'GET':
        return render(request, 'signup_user.html')


    elif request.method == 'POST':
        new_phone_number = get_phone_number(request)
        # new_phone_number = request.POST['phoneNumberInput']
        first_password = request.POST['fPassword']
        second_password = request.POST['sPassword']
        if first_password == second_password:
            try:
                new_user = User.objects.create_user(username=new_phone_number, password=first_password)
                new_user.save()
                login(request, new_user)
                return redirect('users:firstPage')
            except IntegrityError:
                return render(request, 'signup_user.html', {'error': "<< This phone number is already signed up! >>"})
        else:
            return render(request, 'signup_user.html', {'error': "The passwords don't match!"})



@login_required
def logout_user_and_lawyer(request):
    if request.method == 'POST':
        logout(request)
        return redirect('welcomePage')



def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html', )

    elif request.method == 'POST':
        # phone_number = get_phone_number
        phone_number = request.POST['phoneNumberInput']
        password = request.POST['passwordInput']
        user = authenticate(request, username=phone_number, password=password)
        if user is None:
            return render(request, 'login.html', {'error': "Try again!"})
        else:
            login(request, user)
            return redirect('users:firstPage')




def sign_up_lawyer(request):

    if request.method == 'GET':
        return render(request, 'signup_lawyer.html', {'form' : SignupLawyerForm()})

    elif request.method == "POST":
        lawyer_name = request.POST['name']
        lawyer_gender = request.POST['gender']
        lawyer_phone = request.POST['phone']
        lawyer_password = request.POST['password']
        try:

            if models.Lawyer.objects.filter(phone=lawyer_phone).exists():
                return render(request, 'signup_lawyer.html', {
                    'error': 'Phone number already exists. Please use a different number.'
                })

            created_user = User.objects.create_user(username=lawyer_name, password=lawyer_password, )
            created_user.save()

            new_lawyer = models.Lawyer.objects.create(gender=lawyer_gender, phone=lawyer_phone, user=created_user)
            new_lawyer.save()

            login(request, created_user)

            return redirect('users:firstPage')
        except IntegrityError:
            return render(request, 'signup_lawyer.html')



def login_lawyer(request):
    if request.method == "GET":
        return render(request, 'login_lawyer.html')

    elif request.method == "POST":
        phone = request.POST['phone']
        password = request.POST['password']

        # Finding the Lawyer object using its phone(we set the field which we want to find our lawyer based on that in this parenthesis )
        try:
            lawyer = models.Lawyer.objects.get(phone=phone)
            user = lawyer.user      # Get the related User object

            # Check if the password matches
            # if user.password is password:   ===> Not a good condition: raw password input (password) with the stored user.password value, which is hashed in Django
            if user.check_password(password):
                login(request, user)
                return redirect('users:firstPage')
            else:
                return render(request, 'login_lawyer.html', {'error': "Phone or Password is wrong."})

        except models.Lawyer.DoesNotExist:
            return render(request, 'login_lawyer.html', {'error' : "No user with this phone number exists."})




# @login_required
# def logout_lawyer(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('welcomePage')




# THIS METHOD IS FOR CREATING A QUESTION USING DJANGO FORM.
# @login_required
# def create_question_first_page(request):
#     if request.method == 'GET':
#         questions = models.Question.objects.all()
#         return render(request, 'create_Q_first_Page.html', {'form': QuestionForm(), 'questions': questions})
#         # return render(request, 'create_Q_first_Page.html', {'questions': questions})
#
#     elif request.method == 'POST':
#         try:
#             # question_title = request.POST['qTitle']
#             # question_text = request.POST['qText']
#             # new_question =
#             form = QuestionForm(request.POST)
#             if form.is_valid():
#                 new_question = form.save(commit=False)
#                 new_question.user_id = request.user
#                 new_question.save()
#                 return redirect('users:firstPage')
#         except ValueError:
#             return redirect('users:firstPage')
            # return render(request, 'welcome.html', {'form': QuestionForm(), 'error': 'bad data passed in. Try again'})








# THIS METHOD IS FOR CREATING QUESTION WHIT OUT USING DJANGO FORM AND USING HTML TEXT BOX
@login_required
def create_question_first_page(request):

    questions = models.Question.objects.all()

    if request.method == 'GET':
        return render(request, 'create_Q_first_Page.html', {'questions': questions})
        # return render(request, 'create_Q_first_Page.html', {'questions': questions})

    elif request.method == 'POST':

        # this try except is for checking if the user have a lawyer field(the user is lawyer or not)
        try:
            user = request.user.lawyer.base_role

            if user != "Lawyer":
                # this try checks if the the entry value is bad(bad info)
                try:
                    # question_title = request.POST['qTitle']
                    # question_text = request.POST['qText']
                    # new_question =
                    question_title = request.POST.get('qTitle')  # getting question title form html file
                    question_text = request.POST.get('qText')  # getting question text from html file
                    if question_title != "" and question_text != "":
                        models.Question.objects.create(title=question_title, question_text=question_text,
                                                       user=request.user)

                        # new_question = form.save(commit=False)
                        # new_question.user_id = request.user
                        # new_question.save()
                        return redirect('users:firstPage')
                    else:
                        return render(request, 'create_Q_first_Page.html',
                                      {'questions': questions, 'error': ">> Title or Question Text is empty! <<"})
                except ValueError:
                    return redirect("users:firstPage")

            else:
                return render(request, 'create_Q_first_Page.html',
                              {'error': "Lawyers can not ask question like, bro :)", 'questions' : questions})
        except:
            try:
                # question_title = request.POST['qTitle']
                # question_text = request.POST['qText']
                # new_question =
                question_title = request.POST.get('qTitle')  # getting question title form html file
                question_text = request.POST.get('qText')  # getting question text from html file
                if question_title != "" and question_text != "":
                    models.Question.objects.create(title=question_title, question_text=question_text, user=request.user)

                    # new_question = form.save(commit=False)
                    # new_question.user_id = request.user
                    # new_question.save()
                    return redirect('users:firstPage')
                else:
                    return render(request, 'create_Q_first_Page.html',
                                  {'questions': questions, 'error': ">> Title or Question Text is empty! <<"})
            except ValueError:
                return redirect("users:firstPage")


@login_required
def delete_question(request, question_pk):
    question = get_object_or_404(models.Question, pk=question_pk)

    if question is not None:
        question.delete()
        return redirect('users:firstPage')
    else:
        return render(request, 'user_Question.html')



@login_required
def user_question(request, question_pk):
    # question = get_object_or_404(models.Question, pk=question_pk, user_id=request.user)
    question = get_object_or_404(models.Question, pk=question_pk)   # we want to make sure everybody can see others questions but only the created-user can edit own question
    question_answers = models.Answer.objects.filter(question_ans=question)

    is_owner = request.user.id == question.user.id   # we check here if the current user is the one who asked this question(we do this inorder to users can change only their own question)


    # hasattr() is a built-in Python function used to check if an object has a specified attribute.
    # The function returns True if the object has the attribute, and False otherwise.
    # object: The object to check.
    # 'attribute': The name of the attribute as a string.
    is_lawyer = hasattr(request.user, 'lawyer')
    if is_lawyer:
        current_lawyer = request.user.lawyer

    # we pass the question and is_owner to html file
    if request.method == "GET":
        return render(request, 'user_Question.html', {'question': question, 'answers' : question_answers, 'is_owner': is_owner, 'is_lawyer' : is_lawyer, 'current_lawyer' : current_lawyer})
    #
    # elif request.method == "POST":
    #     pass



@login_required
def edit_question(request, question_pk):
    question = get_object_or_404(models.Question, pk=question_pk, user=request.user)

    if request.method == 'GET':
        return render(request, 'edit_question.html', {'question_pk': question_pk})

    elif request.method == 'POST':


        question_title = request.POST.get('qTitle').strip()     # deletes all the " " of the title(left and right of the title)
        question_text = request.POST.get('qText').strip()       # deletes all the " " of the text (left and right of the text)

        if question.title != "" and question_text != "":
            question.title = question_title
            question.question_text = question_text

            question.save()

            return redirect('users:userAskedQuestionPage', question_pk = question_pk)   # for redirecting to userAskedQuestion we have to return the question_pk too (because This part provides
            # a keyword argument to the URL that is being redirected to. If you look at users:userAskedQuestionPage url in urls.py you will notice that in that url we need a question_pk argument)
        else:
            return render(request, 'edit_question.html', {'question_pk': question_pk, 'error': ">> Title or Question Text is empty! <<"})



@login_required
def answer_questions(request, question_pk):

    question = get_object_or_404(models.Question, pk=question_pk)

    if request.method == 'GET':
        return render(request, 'answer_question.html', {'question': question,'question_pk' : question_pk})

    elif request.method == "POST":
        answer_text = request.POST['aText']

        if answer_text != "":
            question_answer = models.Answer.objects.create(answer=answer_text, lawyer=request.user.lawyer, question_ans=question)
            question_answer.save()
            return redirect("users:userAskedQuestionPage", question_pk = question_pk)
        else:
            return render(request, 'answer_question.html', {'question' : question, 'error' : "Invalid Answer"})



@login_required
def edit_answer(request, answer_pk):

    answer = get_object_or_404(models.Answer, pk=answer_pk)

    if request.method == "GET":
        return render(request, 'edit_answer.html', {'answer_pk' : answer_pk, 'last_answer' : answer.answer})

    elif request.method == "POST":
        answer_text = request.POST['ansText']
        if answer_text != "":
            answer.answer = answer_text
            answer.save()
            return redirect("users:userAskedQuestionPage", question_pk=answer.question_ans.id)      # because we redirect to userAskedQuestion, and userAskedQuestion need a question_pk we have to give it the question.id. We get the question.id by answer(answer is related to question)
        else:
            return render(request, 'edit_answer.html', {'error' : "Invalid answer!"})




@login_required
def delete_answer(request, answer_pk):
    if request.method == 'POST':
        answer = get_object_or_404(models.Answer, pk=answer_pk)
        answer.delete()
        return redirect('users:userAskedQuestionPage', answer.question_ans.id)



# @csrf_exempt  # To allow POST requests from the frontend without CSRF token for simplicity (use carefully)
# def send_sms(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         phone_number = data.get('phoneNumber', '')
#
#         client = Client(keys.account_sid, keys.auth_token)
#
#         if phone_number:
#             try:
#                 # Send SMS via Twilio
#                 message = client.messages.create(
#                     body="Hello, this is a test SMS from Django!",
#                     from_='+1234567890',  # Your Twilio phone number
#                     to=phone_number
#                 )
#                 return JsonResponse({'message': 'SMS sent successfully!', 'sid': message.sid}, status=200)
#             except Exception as e:
#                 return JsonResponse({'error': str(e)}, status=500)
#         else:
#             return JsonResponse({'error': 'Phone number not provided'}, status=400)
#
#     return JsonResponse({'error': 'Invalid request method'}, status=405)



def get_phone_number(request):
    if request.method == "GET":
        return render(request, 'signup_user.html')
    if request.method == "POST":
        new_phone_number = request.POST['phoneNumberInput']
        return new_phone_number

        # if new_phone_number.isdigit() and new_phone_number.startswith("98") and len(new_phone_number) == 12:
        #     return new_phone_number
        # else:
        #     print("Invalid phone number. Please enter a 12-digit number starting with the country code '98'.")



