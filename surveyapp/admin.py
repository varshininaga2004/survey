from django.contrib import admin
from .models import Question, Result

# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
    search_fields = ['text']

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'yes_count', 'no_count', 'not_interested_count']