from django.contrib import admin
from .models import Question , Answer

# Register your models here.

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer_content', 'created_at', 'answer_lawyer', 'answer_rate', 'question_id', )

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_title', 'created_at', 'question_text', 'question_url', )


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
