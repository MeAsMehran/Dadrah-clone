from django.contrib import admin

from my_core.models import Question

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('date', )  # this is read-only field we can see in the django admin page. the models other field are changeable by admin but the date is not


admin.site.register(Question, QuestionAdmin)



