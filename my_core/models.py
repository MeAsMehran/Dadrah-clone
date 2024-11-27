from django.db import models
from my_users.models import NormalUser, Lawyer
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.




# class NormalUserFunctions:

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, verbose_name='Question Title', blank=False)
    question_text = models.TextField(max_length=1000, verbose_name='Question Text', blank=False)
    date = models.DateField(auto_now_add=True, blank=False)
    # user_id = models.ForeignKey('my_users.NormalUser', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class InPersonConsultationUser(models.Model):
    id = models.AutoField(primary_key=True)
    province = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    subject = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True, blank=False, null=True)
    # lawyer_id = models.ForeignKey('my_users.Lawyer', on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    lawyer = models.ForeignKey('my_users.Lawyer', on_delete=models.CASCADE, null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class PhoneConsultationUser(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=200, blank=False)
    subject = models.CharField(max_length=1000, blank=False)
    # lawyer_id = models.ForeignKey('my_users.Lawyer', on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)







class CheckingDocuments(models.Model):
    pass

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    payment_conditions = [('pending', 'Pending'), ('successful', 'Successful'), ('failed', 'Failed')]

    amount = models.DecimalField(max_length=12, decimal_places=2, max_digits=10)
    description = models.TextField(max_length=500, blank=True)
    payment_gate = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=20, choices=payment_conditions, default='pending')
    transaction_id = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user_id = models.ForeignKey('my_users.NormalUser', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    # payment_status = models.CharField(max_length=20,
    #                           choices=[('pending', 'Pending'), ('successful', 'Successful'), ('failed', 'Failed')],
    #                           default='pending')

class Notifications(models.Model):      # ????????
    pass

class Tickets(models.Model):
    id = models.AutoField(primary_key=True, )
    ticket_license = models.CharField(max_length=10, blank=False, )
    title = models.CharField(max_length=500, blank=False, )
    date = models.DateField(auto_now_add=True, )
    time = models.TimeField(auto_now_add=True, )
    # user_id = models.ForeignKey('my_users.NormalUser', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, )




# class LawyerFunctions:

class Answer(models.Model):
    # id = models.AutoField(primary_key=True)
    answer = models.TextField(max_length=1500, verbose_name='Answer', blank=False)
    date = models.DateField(auto_now_add=True, blank=False)
    time = models.DateTimeField(auto_now_add=True, blank=False)
    # lawyer = models.ForeignKey('my_users.Lawyer',related_name='answer', on_delete=models.CASCADE, default=)
    lawyer = models.ForeignKey('my_users.Lawyer', related_name='answer', on_delete=models.CASCADE, null=True, blank=True)
    question_ans = models.ForeignKey(Question, on_delete=models.CASCADE, )
    # rate = models.IntegerField(default=0, blank=True, null=True)
    def average_rating(self):
        ratings = self.ratings.all()
        total_ratings = ratings.count()  # Get the count of ratings

        if total_ratings > 0:
            # Calculate average if there are ratings
            return round(sum(rating.rating for rating in ratings) / total_ratings, 1)
        else:
            # Return 0 if there are no ratings
            return 0

        # return sum(rating.rating for rating in ratings) / ratings.count() if ratings.exists() else 0

    def __str__(self):
        return self.answer


class Rating(models.Model):
    class StarRating(models.IntegerChoices):
        ONE = 1, _('1 Star')
        TWO = 2, _('2 Stars')
        THREE = 3, _('3 Stars')
        FOUR = 4, _('4 Stars')
        FIVE = 5, _('5 Stars')

    answer = models.ForeignKey(Answer, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=StarRating.choices)

    class Meta:
        unique_together = ('answer', 'user')

    def __str__(self):
        return f"Rating {self.rating} for {self.answer.id} by {self.user.username}"

class Degree(models.Model):
    id = models.AutoField(primary_key=True  )
    title = models.CharField(max_length=100, blank=False)
    university = models.CharField(max_length=200, blank=False)
    # lawyer_id = models.ForeignKey('my_users.Lawyer', on_delete=models.CASCADE)


class Skills(models.Model):
    id = models.AutoField(primary_key=True, )
    title = models.CharField(max_length=75, blank=True)
    info = models.TextField(blank=False)


class SocialMedia(models.Model):
    id = models.AutoField(primary_key=True)
    instagram = models.URLField(unique=True, blank=True, )
    telegram = models.URLField(unique=True, blank=True, )
    # lawyer_id = models.ForeignKey('my_users.Lawyer', on_delete=models.CASCADE)


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    province = models.CharField(max_length=50, blank=False, )
    city = models.CharField(max_length=50, blank=True, )
    # lawyer_id = models.ForeignKey('my_users.Lawyer', on_delete=models.CASCADE)


class InPersonConsultationLawyer(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=75, blank=False)
    subject = models.CharField(max_length=1000, blank=False)



class PhoneConsultationLawyer(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=75, blank=False)
    subject = models.CharField(max_length=1000, blank=False)
    # lawyer_id = models.ForeignKey('my_users.Lawyer', on_delete=models.CASCADE)



##################################################################################################
##################################################################################################
##################################################################################################


# class ScrapedQuestion(models.Model):
#     question_title = models.CharField(max_length=64)
#     question_text = models.TextField()
#     question_date = models.DateTimeField()
#     question_url = models.CharField(max_length=64)
#
# class ScrapedAnswer(models.Model):
#     answer_text = models.TextField()
#     answer_date = models.DateTimeField()
#     answer_lawyer = models.CharField(max_length=64)
#     answer_rate = models.FloatField()
#     question = models.ForeignKey(ScrapedQuestion, on_delete=models.CASCADE, related_name='scraped_answers')










