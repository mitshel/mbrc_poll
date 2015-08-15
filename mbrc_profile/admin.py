from django.contrib import admin
from mbrc_profile.models import UserProfile, specialize

class UserProfile_admin(admin.ModelAdmin):
    list_display = ('uid', 'tel', 'employment', 'position', 'specialize', 'last_sms', 'is_confirmed')

# Register your models here.
admin.site.register(UserProfile, UserProfile_admin)
admin.site.register(specialize)
