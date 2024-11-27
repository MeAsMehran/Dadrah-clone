

from django.forms import ModelForm
from my_core.models import Question
from my_core.models import Lawyer
from django import forms


class QuestionForm(ModelForm):       # we put () to inherit
    class Meta:
        model = Question
        fields = ['title', 'question_text']     # we set the fields which we need from the models.py file to be shown in our form for user to fill them



class SignupLawyerForm(ModelForm):
    class Meta:
        model = Lawyer
        fields = ['name', 'gender', 'phone']



class RatingForm(forms.Form):
    rating = forms.ChoiceField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')], widget=forms.RadioSelect)
