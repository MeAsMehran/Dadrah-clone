from django.contrib import admin

from my_users.models import Lawyer

# Register your models here.

# class QuestionAdmin(admin.ModelAdmin):
#     readonly_fields = ('date', )  # this is read-only field we can see in the django admin page. the models other field are changeable by admin but the date is not
#
#
# admin.site.register(Question, QuestionAdmin)

class LawyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'base_role', 'name', 'password', 'gender', 'phone', 'user')



admin.site.register(Lawyer, LawyerAdmin)