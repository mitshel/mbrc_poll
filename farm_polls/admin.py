from django.contrib import admin
from farm_polls.models import anketa, poll, preparat, question

class anketa_admin(admin.ModelAdmin):
    list_display = ('name', 'specialize')

class poll_admin(admin.ModelAdmin):
    list_display = ('name', 'anketa')

class question_admin(admin.ModelAdmin):
    list_display = ('name', 'poll', 'pos','answer_type', 'checkbox_limit', 'combobox_csv')

class preparat_admin(admin.ModelAdmin):
    list_display = ('name', 'poll')

# Register your models here.
admin.site.register(anketa, anketa_admin)
admin.site.register(poll, poll_admin)
admin.site.register(question, question_admin)
admin.site.register(preparat, preparat_admin)