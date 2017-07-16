# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class MyUser(models.Model):
	user_id = models.OneToOneField(User)
	area = models.CharField(max_length=20, blank=True, null=True)
	tarrif = models.CharField(max_length=20, blank=True, null=True)

# Use signal to create profile for the user when the user created
def create_new_user(sender, **kwargs):
	if kwargs['created']:
		user_profile = MyUser.objects.create(user=kwargs['instance'])

post_save.connect(create_new_user, sender=User)