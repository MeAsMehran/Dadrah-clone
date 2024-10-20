from django.db import models

from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser


# from django.contrib.auth.base_user import BaseUserManager
# from my_core.models import NormalUserFunctions , LawyerFunctions
# Create your models here.


# managements methods will get a query set from the my_users based on their user type
# class NormalUserManagement(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(args, **kwargs)
#         return results.filter(role=Users.Role.NORMAL_USER)


# class LawyersManagement(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(role=Users.Role.LAWYER)


# *****************************     this User class is using top level packages (not recommended)
# changing the base for creating my_users(manipulating the abstractUser class)
# class Users(AbstractUser):

# Defining user roles:
# class Role(models.TextChoices):
#     ADMIN = 'ADMIN', 'admin'
#     NORMAL_USER = 'NORMAL_USER', 'normalUser'      # the first one is the value and saved in data base and the second one is human-readable label
#     LAWYER = 'LAWYER', 'lawyer'


# base role is Admin
# base_role = Role.ADMIN

# Determining the user role by using choices in Role Class
# role = models.CharField(max_length=50, choices=Role.choices)

# creating a default method for creating a user
# def save(self, *args, **kwargs):
#     if not self.pk:     # user don't have the primary key which means not signed up yet.
#         self.role = self.base_role
#         return super().save(*args, **kwargs)


class NormalUser(models.Model):
    id = models.AutoField(primary_key=True)

    base_role = "NormalUser"  # for specifying the normal my_users and lawyers (specifying the user type)

    # normal_user = NormalUserManagement()

    # Phone number field:
    phone = models.CharField(max_length=10, unique=True,
                             help_text='09xx xxx xxxx', blank=False, null=False,
                             error_messages={'unique': 'The phone number is already in use.'}, )

    password = models.CharField(max_length=10, blank='default_password')

    # Number verification field:
    is_verified = models.BooleanField(default=False, blank=False,
                                      help_text='Designates whether this user has verified phone', )

    # in_person_consultation = models.ForeignKey(NormalUserFunctions.InPersonConsultation, on_delete=models.CASCADE)
    # phone_consultation = models.ForeignKey(NormalUserFunctions.PhoneConsultation, on_delete=models.CASCADE)
    # documents = models.ForeignKey(NormalUserFunctions.InPersonConsultation, on_delete=models.CASCADE)
    # lawyer_history = models.ForeignKey('Lawyer', on_delete=models.CASCADE)
    # questions = models.ForeignKey(NormalUserFunctions.Question, on_delete=models.CASCADE)
    # transaction = models.ForeignKey(NormalUserFunctions.Transaction, on_delete=models.CASCADE)
    # comments =

    # def welcome(self):
    #     return "only for NormalUsers"

    def __Str__(self):
        return self.phone


class Lawyer(models.Model):
    id = models.AutoField(primary_key=True)
    base_role = "Lawyer"  # for specifying the normal my_users and lawyers (specifying the user type)

    name = models.CharField(max_length=200, )
    password = models.CharField(max_length=10, blank=True, null=True, )
    gender = models.CharField(max_length=6, choices=[('female', 'Female'), ('male', 'Male')], default='male',
                              blank=False)
    phone = models.CharField(max_length=10, unique=True, help_text="09xx xxx xxxx", blank=False,
                             error_messages={'unique': 'The phone number is already in use.'}, )
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    is_verified = models.BooleanField(default=False, blank=False,
                                      help_text="Designates whether this lawyer has verified phone", )
    license_number = models.CharField(max_length=5, blank=True)  # shomare parvande
    history_of_legal_license = models.CharField(max_length=50, blank=True)  # دارای سابقه پروانه وکالت
    # location = models.CharField(max_length=200, verbose_name="استان", blank=False, )                                      # how to use menu button for choosing the city and save it here?
    # degree = models.CharField(max_length=1000, blank=False, )
    about_me = models.TextField(max_length=1000, blank=True, )
    # case_history = models.ForeignKey(NormalUserFunctions.Question, on_delete=models.CASCADE)                     # savabegh
    # telegram = models.URLField(unique=True, blank=True, )
    # instagram = models.URLField(unique=True, blank=True, )
    # skills = models.ForeignKey(LawyerFunctions.Skills, related_name='skills', on_delete=models.CASCADE)

    # in_person_consultation_history = models.ForeignKey()
    # phone_consultation_history =

    img = models.ImageField(upload_to="", blank=True, help_text="Set profile picture", verbose_name="Profile Picture", )

    def __str__(self):
        return self.name