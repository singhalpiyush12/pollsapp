from django.contrib import admin
from polls.models import Question,Choice
# Register your models here.
class ChoiceInLine(admin.TabularInline):
	model=Choice
	extra=3
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 		{'fields':['question_text']}),
		('Date information', {'fields':['pub_date'],'classes':['collapse']}),
	]
	list_filter=['pub_date']
	inlines=[ChoiceInLine]
	search_field=['question_text']
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
