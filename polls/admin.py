from django.contrib import admin
from polls.models import UserProfile, polls, polls_Questions, polls_Answers, polls_Results, polls_AnswersResults, specialize

class polls_admin(admin.ModelAdmin):
    list_display = ('name', 'specialize')

class polls_Questions_admin(admin.ModelAdmin):
    list_display = ('question', 'poll')

# Register your models here.
admin.site.register(polls, polls_admin)
admin.site.register(polls_Questions, polls_Questions_admin)
admin.site.register(polls_Answers)
admin.site.register(polls_Results)