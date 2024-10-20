

from django.forms import ModelForm
from my_core.models import Question
from my_core.models import Lawyer


class QuestionForm(ModelForm):       # we put () to inherit
    class Meta:
        model = Question
        fields = ['title', 'question_text']     # we set the fields which we need from the models.py file to be shown in our form for user to fill them



class SignupLawyerForm(ModelForm):
    class Meta:
        model = Lawyer
        fields = ['name', 'gender', 'phone']

