# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# Register your models here.

from .models import Consumption


class ConsumptionAdmin(admin.ModelAdmin):
	class Meta:
		model = Consumption
		fields = ('create_date_time', 'consumption')

admin.site.register(Consumption, ConsumptionAdmin)