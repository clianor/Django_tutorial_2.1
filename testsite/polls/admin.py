from django.contrib import admin

from .models import Question, Choice

# Register your models here.
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice    # Choice 모델을 이용.
    extra = 1    # 기본으로 1가지 항목을 제공.
# end class

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    fieldsets = [
        (None, {'fields' : ['question_text']}),
        ('Date Infomation', {'fields' : ['pub_date']}),
    ]
    inlines = [ChoiceInline]

    list_filter = ['pub_date']
# end class

admin.site.register(Question, QuestionAdmin)