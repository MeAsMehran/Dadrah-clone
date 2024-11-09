from django.contrib import admin

from my_core.models import Answer , Question

# Register your models here.

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'get_lawyer_name', 'date')
    readonly_fields = ('date', )  # this is read-only field we can see in the django admin page. the models other field are changeable by admin but the date is not

    def get_lawyer_name(self, obj):
        return obj.lawyer.name if obj.lawyer else 'No Lawyer'
    get_lawyer_name.short_description = 'Lawyer'



class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('date', )  # this is read-only field we can see in the django admin page. the models other field are changeable by admin but the date is not




admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)







