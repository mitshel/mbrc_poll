from django.contrib import admin
from polls.models import UserProfile, polls, polls_Questions, polls_Answers, polls_Results, polls_AnswersResults, specialize

class polls_admin(admin.ModelAdmin):
    list_display = ('name', 'specialize')

class polls_Questions_admin(admin.ModelAdmin):
    list_display = ('question', 'poll')

class UserProfile_admin(admin.ModelAdmin):
    list_display = ('uid', 'tel', 'employment', 'position', 'specialize', 'last_sms', 'is_confirmed')


# Register your models here.
admin.site.register(UserProfile, UserProfile_admin)
admin.site.register(specialize)
admin.site.register(polls, polls_admin)
admin.site.register(polls_Questions, polls_Questions_admin)
admin.site.register(polls_Answers)
admin.site.register(polls_Results)