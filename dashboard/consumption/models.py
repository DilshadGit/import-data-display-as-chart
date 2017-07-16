# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models
from accounts.models import MyUser

# Create your models here.
class Consumption(models.Model):
	user_id = models.IntegerField(default=0, blank=True, null=True)
	create_date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	consumption = models.DecimalField(null=True, blank=True, default=0, max_digits=6, decimal_places=2)

	def __unicode__(self):
		return str(self.consumption)