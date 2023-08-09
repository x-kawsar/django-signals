from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver

class Profile(models.Model):
    user       = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name  = models.CharField(max_length=50, null=True, blank=True)
    phone      = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self):
        return str(self.user)
