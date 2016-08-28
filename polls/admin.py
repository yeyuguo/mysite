from django.contrib import admin

# Register your models here.


# choice table
from .models import Choice
# 1.
# admin.site.register(Choice)
# 4.
# class ChoiceInline(admin.StackedInline):
# 	model = Choice
# 	extra = 3
# 4. table: inline-block
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


from .models import Question
# 1.
# admin.site.register(Question)
# 2.
# class QuestionAdmin(admin.ModelAdmin):
# 	fields = ['pub_date','question_text']
# admin.site.register(Question,QuestionAdmin)

# 3.
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('wo xiang tianjia de xinxi',               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'],'classes': ['collapse']}),
#     ]

# 4.
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [

#         ('wo xiang tianjia de xinxi',               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'],'classes': ['collapse']}), # 'classes' is html's style
#     ]
#     inlines = [ChoiceInline]
# 4.
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('question_text', 'pub_date')
#     inlines = [ChoiceInline]
# 4.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text'] # filter
    inlines = [ChoiceInline]



admin.site.register(Question, QuestionAdmin)





