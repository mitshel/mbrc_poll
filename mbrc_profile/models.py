from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class specialize(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    uid = models.OneToOneField(User, null=True)
    specialize = models.ForeignKey(specialize, null=True)
    tel = models.CharField(max_length=10)
    o = models.CharField(max_length=32, null=True)
    employment = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    ranks = models.CharField(max_length=256)
    last_sms = models.CharField(max_length=6, null=True)
    last_sms_time = models.DateTimeField(null=True)
    n_sms = models.IntegerField(default=0)
    is_confirmed = models.BooleanField(default=False)
    activation_key = models.CharField(max_length=40, blank=True)
    key_send_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.uid.username

    class Meta:
        verbose_name_plural=u'User profiles'